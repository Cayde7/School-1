import datetime as dt
import psycopg2


# Connect met de database
con = psycopg2.connect(
    host='localhost',       # Host IP adres
    database='NStweets',    # Database name
    user='postgres',        # Database user, default is postgres
    password='post'     # Password to access database
    # port=5432 # Uncomment if you want to use a port other than the default
)

# Create file "station.dat" if it doesn't excist
def read_station():
    try:
        with open("station.dat", "r") as f:
            return f.read()
    except FileNotFoundError:
        with open("station.dat", "w") as f:
            huidigstation = input("First time setup\n\nStation naam: ")
            cur = con.cursor()
            cur.execute(("SELECT * FROM station WHERE stationnaam = '{}'").format(huidigstation))
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
login(8)
# Accept tweet
def accept_tweet(tweetid, moderator):
    cur = con.cursor()
    cur.execute("UPDATE tweet SET geaccepteerd = True WHERE tweetid = %s", (tweetid,))
    cur.execute("UPDATE tweet SET moderatormoderatorid = %s WHERE tweetid = %s", (moderator, tweetid))
    cur.execute("UPDATE tweet SET moddatum = %s WHERE tweetid = %s", (dt.datetime.now(), tweetid))
    cur.execute("UPDATE tweet SET modtijd = %s WHERE tweetid = %s", (dt.datetime.now().strftime("%H:%M:%S"), tweetid))
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

"""
cur = con.cursor()
cur.execute("select * from bericht")
# Uitvoer query. Hier vullen we de database met gegevens
# Door de constructie met (%s, %s, %s), (attribuut, attribuut, attribuut)) zetten we alleen maar strings erin
# die we later toewijzen. Hierdoor kunnen we de database vullen zonder steeds de code aan te moeten passen.
# Deze manier is ook veiliger dan gelijk values (attribuut, attribuut, attribuut)).
cur.execute('insert into tabel (attribuut, attribuut, attribuut) values (%s, %s, %s)',
                (attribuut, attribuut, attribuut))
# Je wilt alles fetchen van de query die je hebt uitgevoerd
rows = cur.fetchall()
# Forloop die alles in elke row steeds alle colums af gaat. Per column die je hebt, moet je een {r[index]}
# toevoegen om hem te printen
for r in rows:
    print(f"atribuut {r[0]} atribuut {r[1]}")
# Sluit de cursor
cur.close()
# Sluit de database connectie
con.close()
"""

"""
def checktweetsfile(tweetsFile):
    if not os.path.isfile(tweetsFile):
        tweets = open(tweetsFile, "w")
        tweets.close()


def gettweets(tweetsFile):
    tweets = open(tweetsFile, "r")
    tweetsList = tweets.read().split("\n")
    tweets.close()
    return tweetsList

def mostrecenttweet(tweetsFile):
    tweets = open(tweetsFile, "r")
    tweetsList = tweets.read().split("\n")
    tweets.close()
    return tweetsList[-1]


def deletetweetcontainingword(tweetsFile, word):
    tweets = open(tweetsFile, "r")
    tweetsList = tweets.read().split("\n")
    tweets.close()
    tweets = open(tweetsFile, "w")
    for tweet in tweetsList:
        if word not in tweet:
            tweets.write(tweet + "\n")
    tweets.close()

def deletetweet(tweetsFile, index):
    tweets = open(tweetsFile, "r")
    tweetsList = tweets.read().split("\n")
    tweets.close()
    tweets = open(tweetsFile, "w")
    for tweet in tweetsList:
        if index != tweetsList.index(tweet):
            tweets.write(tweet + "\n")
    tweets.close()

def addtweet(tweetsFile, name, tweet):
    if len(tweet) > 140:
        print(f"Tweet is te lang! {len(tweet)}/140")
        return 1
    elif len(tweet) < 1:
        print("Tweet is leeg!")
        return 2
    elif len(tweet) == 10:
        print("Tweet is te kort!")
        return 3
    elif len(name) > 20:
        print("Naam is te lang!")
        return 4
    elif len(name) < 1:
        name = "Anoniem"
    tweets = open(tweetsFile, "a")
    datetime = str(dt.datetime.now())
    tweets.write(name + ";" + tweet + ";" + datetime + "\n")
    tweets.close()
    return 0


def showtweets(tweetsFile):
    tweets = open(tweetsFile, "r")
    print(tweets.read())
    tweets.close()
"""