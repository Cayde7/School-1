import TweetActions as TA
import tkinter as TK
# from PIL import ImageTk, Image
import psycopg2
import pyowm

# Connect the database
con = psycopg2.connect(
    host='localhost',  # Host IP adres
    database='NStweets',  # Database name
    user='postgres',  # Database user, default is postgres
    password='post'  # Password to access database
    # port=5432 # Uncomment if you want to use a port other than the default
)

# Get Station
station = TA.read_station()

# Create main window
MainWindow = TK.Tk()
MainWindow.title("Twitter Scherm")

# Get screen width and height
screen_width = MainWindow.winfo_screenwidth()
screen_height = MainWindow.winfo_screenheight()
print(f"Kanker; {TA.get_sent_tweets(station)}")
# Variable stuff
Tweet_index = 0
Tweets = TA.get_sent_tweets(station)
for tweet in Tweets:
    print(tweet)
owm = pyowm.OWM('15988220a0bc95a2c424bbd459c12dbb')

#Get weather from API and return temp in celsius
def get_weather(station):
    Location = owm.weather_manager().weather_at_place(station.split(' ')[0])
    print(Location)
    return Location.weather.temperature('celsius')['temp']

# Function to display the first or next tweet
def Refresh_Display(Tweet_index, Tweets):
    Tweet_index += 1
    if Tweet_index == len(Tweets):
        TA.get_sent_tweets(station)
        Tweet_index = 0
    # Clear the display
    destroy_layout()
    MainWindow.grid()
    # Create Tweet display
    TweetDisplay(Tweets, Tweet_index)




# Create Tweet display
def TweetDisplay(Tweets, Tweet_index):
    # Blank space
    TK.Label(MainWindow, text='', background='#FFC917').grid(row=0, column=0, padx=10, pady=10)
    TK.Label(MainWindow, text='', background='#FFC917').grid(row=0, column=4, padx=10, pady=10)

    # Create Tweet name
    Tweet_Name = TK.Label(MainWindow,
                       text=Tweets[Tweet_index][2],
                       font=("NS Sans Bold", 36),
                       foreground='#333399', background='#FFC917',
                       anchor='w')
    Tweet_Name.grid(row=1, column=1, columnspan=3, sticky='news')

    # Create Tweet text
    Tweet_text = TK.Label(MainWindow,
                          text=Tweets[Tweet_index][4],
                          font=("NS Sans", 36),
                          wraplength=1269,
                          foreground='#333399')
    Tweet_text.grid(row=2, column=1, columnspan=3, sticky='news')

    # Create weather label
    Weather = TK.Label(MainWindow,
                          text=f'{round(get_weather(station)*10)/10}°C in {station.split(" ")[0]}',
                          font=("NS Sans", 36),
                          foreground='#333399', background='#FFC917',
                          anchor='e')
    Weather.grid(row=3, column=3, sticky='news')

    MainWindow.rowconfigure(0, weight=1)
    MainWindow.rowconfigure(1, weight=0)
    MainWindow.rowconfigure(2, weight=1)
    MainWindow.rowconfigure(3, weight=0)
    MainWindow.rowconfigure(4, weight=1)
    MainWindow.columnconfigure(0, weight=1)
    MainWindow.columnconfigure(1, weight=1)
    MainWindow.columnconfigure(2, weight=1)
    MainWindow.columnconfigure(3, weight=1)
    MainWindow.columnconfigure(4, weight=1)
    MainWindow.after(10000, lambda: Refresh_Display(Tweet_index, Tweets))


def destroy_layout():
    # Destroy all widgets
    for widget in MainWindow.winfo_children():
        widget.destroy()

Refresh_Display(Tweet_index, Tweets)
# execute MainWindow
MainWindow.attributes('-fullscreen', True)
MainWindow.configure(background='#FFC917')
MainWindow.protocol("WM_DELETE_WINDOW", con.close())
MainWindow.mainloop()