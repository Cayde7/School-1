import datetime as dt
import psycopg2
from TwitterAPI import TwitterAPI

# Connect met de database
con = psycopg2.connect(
    host='localhost',       # Host IP adres
    database='NStweets',    # Database name
    user='postgres',        # Database user, default is postgres
    password='post'     # Password to access database
    # port=5432 # Uncomment if you want to use a port other than the default
)

# Twitter API info
consumer_key = 'FNzhdGrry5zu0JDSHMYg0BfmM'
consumer_secret = 'Uq2gfL6sJhwcNhDypyRBTqx80SN1JWd8FoqhxM1GYNVx68IW5u'
access_token_key = '1054486066965725184-Zb8H5vs0ZBmlzKcw6fE0TxvybpzYTA'
access_token_secret = '1PoppmWrezTFVumWSxTMuMEg3JdXrlajUAfc6uj6Ib08U'
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# Create file "station.dat" if it doesn't excist
def read_station():
    try:
        with open("station.dat", "r") as f:
            return f.read()
    except FileNotFoundError:
        with open("station.dat", "w") as f:
            huidigstation = input("First time setup\n\nStation naam: ")
            cur = con.cursor()
            cur.execute(("SELECT * FROM stations WHERE stationnaam = '{}'").format(huidigstation))
            if cur.fetchone() is None:
                print("Station niet gevonden!")
                station = open('station.dat', 'w')
                huidigstation = input("First time setup\n\nStation naam: ")
                station.write(huidigstation)
                return read_station()
            else:
                f.write(huidigstation)
                f.close()
                return huidigstation



def highest_tweet_ID():
    cur = con.cursor()
    cur.execute("SELECT MAX(tweetid) FROM tweet")
    return_highest_tweet_ID = cur.fetchone()
    cur.close()
    return return_highest_tweet_ID[0]

# Open cursor and add tweetid, naam, datum, inhoud en stationnaam aan database met tabel bericht
def add_tweet(naam, inhoud, stationnaam):
    tweetid = highest_tweet_ID()
    if tweetid is None:
        tweetid = 0
    tweetid = tweetid + 1
    datum = dt.datetime.now()
    cur = con.cursor()
    cur.execute("INSERT INTO tweet (tweetid, naam, datum, inhoud, stationnaam) VALUES (%s, %s, %s, %s, %s)",
                (tweetid, naam, datum, inhoud, stationnaam))
    con.commit()
    cur.close()

# Open cursor and get the oldest tweet where geaccepteerd is input
def get_unmoderated_tweet():
    cur = con.cursor()
    cur.execute("SELECT * FROM tweet WHERE geaccepteerd IS NULL ORDER BY datum ASC LIMIT 1")
    return_tweet = cur.fetchone()
    cur.close()
    return return_tweet

# Open cursor and get the tweet by ID
def get_tweet(tweetid):
    cur = con.cursor()
    cur.execute("SELECT * FROM tweet WHERE tweetid = %s", (tweetid,))
    return_tweet = cur.fetchone()
    cur.close()
    return return_tweet

# Open cursor and check if username exists in database
def login(username):
    cur = con.cursor()
    try:
        username = int(username)
    except ValueError:
        return 'err_not_an_int'
    cur.execute("SELECT moderatorid FROM moderator WHERE moderatorid = %s", (username,))
    return_user = cur.fetchone()
    cur.close()
    if return_user is None:
        return 'err_username_not_found'
    else:
        return return_user
    # this is where a password check could go in the future
    # if password == password_from_database:
    #     return True
    # else:
    #     return False

# Accept tweet
def accept_tweet(tweetid, moderator):
    cur = con.cursor()
    cur.execute("UPDATE tweet SET geaccepteerd = True WHERE tweetid = %s", (tweetid,))
    cur.execute("UPDATE tweet SET moderatormoderatorid = %s WHERE tweetid = %s", (moderator, tweetid))
    cur.execute("UPDATE tweet SET moddatum = %s WHERE tweetid = %s", (dt.datetime.now(), tweetid))
    cur.execute("UPDATE tweet SET modtijd = %s WHERE tweetid = %s", (dt.datetime.now().strftime("%H:%M:%S"), tweetid))

    # After updating the database, send the Tweet to Twitter
    tweet = get_tweet(tweetid)
    r = api.request('statuses/update', {'status': tweet[4]})
    print(r.status_code)
    con.commit()
    cur.close()

# Deny tweet
def deny_tweet(tweetid, moderator, reason):
    cur = con.cursor()
    cur.execute("UPDATE tweet SET geaccepteerd = False WHERE tweetid = %s", (tweetid,))
    cur.execute("UPDATE tweet SET moderatormoderatorid = %s WHERE tweetid = %s", (moderator, tweetid))
    cur.execute("UPDATE tweet SET moddatum = %s WHERE tweetid = %s", (dt.datetime.now(), tweetid))
    cur.execute("UPDATE tweet SET modtijd = %s WHERE tweetid = %s", (dt.datetime.now().strftime("%H:%M:%S"), tweetid))
    cur.execute("UPDATE tweet SET modreden = %s WHERE tweetid = %s", (reason, tweetid))
    con.commit()
    cur.close()
    # Is there no faster way to do this? // No time to find out, crunch time


# Get all recent tweets from database
def get_sent_tweets(station):
    print(f"Station: {station}")
    cur = con.cursor()
    cur.execute("SELECT * FROM tweet WHERE geaccepteerd IS True AND stationnaam = %s ORDER BY moddatum ASC, modtijd ASC LIMIT 10", (station,))
    return_tweets = cur.fetchall()
    cur.close()
    print(f"Output: \n {return_tweets}")
    return return_tweets

