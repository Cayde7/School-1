import TweetActions as TA
import tkinter as TK
from PIL import ImageTk, Image
import psycopg2

# Connect met de database
con = psycopg2.connect(
    host='localhost',  # Host IP adres
    database='NStweets',  # Database name
    user='postgres',  # Database user, default is postgres
    password='post'  # Password to access database
    # port=5432 # Uncomment if you want to use a port other than the default
)

station = TA.read_station()

# Create a window
MainWindow = TK.Tk()
MainWindow.title("NS Twitter Input Applicatie")

# Get screen width and height
screen_width = MainWindow.winfo_screenwidth()
screen_height = MainWindow.winfo_screenheight()

# Take NS logo and resize it to fit the screen
# FUTURE: animate the logo with some kind of pulse animation to grab people's attention // PS: No, TKinter is not that great for this
NSlogo = Image.open("NStweetsMAX.png")
NSlogo = NSlogo.resize((int(screen_height / 1.3), int(screen_height / 1.3)), Image.ANTIALIAS)
NSlogo = ImageTk.PhotoImage(NSlogo)  # Resize the logo by a factor of 1.3 and antialias it, save that as a var


def welcome_screen():
    # Destroy all widgets
    destroy_layout()

    # Create button with image and make it sticky
    Welcomebutton = TK.Button(master=
                              MainWindow,
                              image=NSlogo,
                              background='#FFC917',
                              anchor='center',
                              command=input_screen)
    Welcomebutton.grid(row=0,
                       column=0,
                       sticky='nsew')

    """
    Not needed because of `MainWindow.attributes('-fullscreen', True)` at the end of the file.
    # width x height + x position + y position
    # %d = decimal placeholder, +0+0 = position
    # https://stackabuse.com/python-string-interpolation-with-the-percent-operator/
    # f"{screen_width}x{screen_height}+0+0" could be an alternative
    # MainWindow.geometry("%dx%d+0+0" % (screen_width, screen_height))"""

    # Add weights so the button fills the whole screen
    MainWindow.columnconfigure(0, weight=1)
    MainWindow.rowconfigure(0, weight=1)
    MainWindow.rowconfigure(1, weight=0)
    MainWindow.rowconfigure(2, weight=0)
    # This is needed or stuff breaks!
    MainWindow.columnconfigure(1, weight=0)
    MainWindow.columnconfigure(2, weight=0)
    MainWindow.columnconfigure(3, weight=0)

def input_screen():
    # Destroy all widgets
    destroy_layout()
    # Create an empty label -- THIS WAS NOT NEEDED FOR SOME REASON?
    # Possibly due to the the layouts done at the end of the function?
    """space_label = TK.Label(master=MainWindow, text="", background='#FFC917')
    space_label.grid(row=0, column=0, sticky='nsew')
    space_label = TK.Label(master=MainWindow, text="", background='#FFC917')
    space_label.grid(row=0, column=2, sticky='nsew')"""

    # Create a label
    label = TK.Label(master=MainWindow,
                     text="Tweet naam (optioneel): ",
                     foreground='#333399', background='#FFC917',
                     font=("NS Sans Bold", 18))
    label.grid(row=0,
               column=1,
               sticky='w', padx=50, pady=50)

    # Create a name textfield
    name = TK.Entry(master=MainWindow,
                    font=("NS Sans", 16))
    name.grid(row=0,
              column=2,
              sticky='e',
              padx=50, pady=50)

    # Create a tweet textbox
    textbox = TK.Text(master=MainWindow,
                      wrap=TK.WORD,
                      font=("NS Sans", 16),
                      width=50, height=10)
    textbox.grid(row=1,
                 column=1,
                 sticky='news',
                 columnspan=2,
                 padx=50, pady=0)
    textbox.focus()  # Thanks to my tester

    # Create a button that checks if the tweet is valid
    button = TK.Button(master=MainWindow,
                       text="\nVerstuur Tweet\n",
                       font=("NS Sans Bold", 16),
                       foreground='#333399', background='#FFC917',
                       command=lambda: post_tweet(name.get(), textbox.get("1.0", "end-1c")))
    button.grid(row=2,
                column=1,
                sticky='news',
                columnspan=2,
                padx=50, pady=50)

    # Layout mess. I hate TKinter, use QT or Kivy next time, might be good.
    MainWindow.columnconfigure(0, weight=1)
    MainWindow.columnconfigure(1, weight=1)
    MainWindow.columnconfigure(2, weight=1)
    MainWindow.columnconfigure(3, weight=1)
    MainWindow.rowconfigure(0, weight=0)
    MainWindow.rowconfigure(1, weight=1)
    MainWindow.rowconfigure(2, weight=0)
    # after 3 minutes, the window will switch to the welcome screen
    MainWindow.after(180000, lambda: welcome_screen())


def post_tweet(naam, tweet):
    # Name check
    if len(naam) > 20:  # Check if the name is valid
        error_popup("Naam is te lang!")
        return False
    elif len(naam) <= 1:  # if no name is given, use anon
        naam = "Anoniem"

    # Tweet check
    if len(tweet) > 140:  # Tweet max length is 140
        error_popup("Tweet is te lang!")
        return False
    elif len(tweet) <= 10:  # Less than 10 characters are often just swearwords or not meaningful content
        error_popup("Tweet is te kort!")
        return False
    else:
        TA.add_tweet(naam, tweet, station)  # Add tweet function, putting this in another file cleans up the UI code
        error_popup("Tweet is verzonden!")  # Thanks to feedback from my mom
        MainWindow.after(3000, lambda: welcome_screen())
        return True


# tkinter.messagebox is a thing... not changing it for now
def error_popup(errormsg):
    # Create a popup window
    error_window = TK.Toplevel(MainWindow)
    error_window.title(errormsg)

    # Set window size and location
    error_window.geometry("300x150+%d+%d" % (screen_width / 2 - 150, screen_height / 2 - 150))

    # Create a error label
    errorlabel = TK.Label(master=error_window,
                          text=errormsg,
                          foreground='#333399', background='#FFC917',
                          font=("NS Sans Bold", 18)) # Font stolen from the internet
    errorlabel.grid(row=0,
                    column=0,
                    sticky='nsew',
                    padx=10, pady=10)

    # Create a button
    errorbutton = TK.Button(master=error_window,
                            text="Ok",
                            command=error_window.destroy,
                            foreground='#333399', background='#FFC917',
                            font=("NS Sans", 16)) # Gosh I wish I had consistency in my code, but its not that important

    errorbutton.grid(row=1,
                     column=0,
                     sticky='nsew',
                     padx=40, pady=10)

    if errormsg == "Tweet is verzonden!":
        error_window.wm_attributes('-fullscreen', 'True') # Hides the window behind and looks nice
        errorlabel.configure(font=("NS Sans Bold", 34)) # Doing it here because my function isn't flexible enough.
        errorbutton.destroy() # No need for a button, useless work to make it work with a button

    # Layout
    error_window.columnconfigure(0, weight=1)
    error_window.rowconfigure(0, weight=1)
    error_window.configure(background='#FFC917')


def destroy_layout():
    # Destroy all widgets
    for widget in MainWindow.winfo_children():
        widget.destroy()


# Start welcomescreen
welcome_screen()

# Execute the window
MainWindow.attributes('-fullscreen', True)
MainWindow.configure(background='#FFC917')
MainWindow.protocol("WM_DELETE_WINDOW", con.close())
MainWindow.mainloop()
