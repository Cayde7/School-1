import TweetActions as TA
import tkinter as TK
from PIL import ImageTk, Image
import psycopg2

# Connect met de database
con = psycopg2.connect(
    host='localhost',       # Host IP adres
    database='NStweets',    # Database name
    user='postgres',        # Database user, default is postgres
    password='post'     # Password to access database
    # port=5432 # Uncomment if you want to use a port other than the default
)

print(TA.get_unmoderated_tweet())

MainWindow = TK.Tk()
MainWindow.title("NS Moderator applicatie")

# Get screen width and height
screen_width = MainWindow.winfo_screenwidth()
screen_height = MainWindow.winfo_screenheight()

# Take NS logo and resize it to fit the screen
NSlogo = Image.open("NSmoderatorMAX.png")
WindowHeight = MainWindow.winfo_screenheight()
NSlogo = NSlogo.resize((int(screen_height / 3), int(screen_height / 3)), Image.ANTIALIAS)
NSlogo = ImageTk.PhotoImage(NSlogo)

MainWindow.columnconfigure(0, weight=1)
MainWindow.rowconfigure(0, weight=1)


def login_check(username):
    # Check if the user is logged in
    TAusername = TA.login(username)
    if str(TAusername[0]) == username:
        destroy_layout()
        global moderator
        moderator = TAusername[0]
        moderation_screen()
    else:
        destroy_layout()
        login_screen()

# Create login screen
def login_screen():
    # Create NS login screen
    NSlogin = TK.Frame(MainWindow,
                       bg="#FFC917")
    NSlogin.grid(row=0,
                 column=0,
                 sticky="nsew",
                 padx=16, pady=16)
    NSlogin.rowconfigure(0, weight=1)
    NSlogin.columnconfigure(0, weight=1)

    # Create NS logo
    NSlogoLabel = TK.Label(NSlogin,
                           image=NSlogo,
                           background='#FFC917')
    NSlogoLabel.grid(row=0,
                     column=0,
                     sticky="nsew")

    # Username label
    UsernameLabel = TK.Label(NSlogin,
                             text="ModeratorID:",
                             font=("Helvetica", 16),
                             foreground='#333399', background='#FFC917',
                             padx=10)
    UsernameLabel.grid(row=1,
                       column=0,
                       sticky="nsew",
                       pady=4)

    # Username entry
    UsernameEntry = TK.Entry(NSlogin,
                             font=("Helvetica", 16),
                             justify="center")
    UsernameEntry.grid(row=2,
                       column=0,
                       sticky="nsew",
                       padx=16, pady=4)

    """
    # Uncomment if password is needed in the future
    # Password label
    PasswordLabel = TK.Label(NSlogin,
                             text="Password:",
                             font=("Helvetica", 16),
                             foreground='#333399', background='#FFC917')
    PasswordLabel.grid(row=3, column=0, sticky="nsew")
    
    # Password entry
    PasswordEntry = TK.Entry(NSlogin,
                             font=("Helvetica", 16),
                             show="*",
                             justify="center")
    PasswordEntry.grid(row=4,
                       column=0,
                       sticky="nsew",
                       padx=16, pady=4)
    """

    # Login button
    LoginButton = TK.Button(NSlogin,
                            text="Login",
                            font=("NS Sans Bold", 16),
                            foreground='#333399', background='#FFC917',
                            command=lambda: login_check(UsernameEntry.get()))
    LoginButton.grid(row=5,
                     column=0,
                     sticky="nsew",
                     padx=64, pady=16)

# Create moderation window
def moderation_screen():
    # Create moderation screen
    Moderation = TK.Frame(MainWindow,
                          bg="#FFC917")
    Moderation.grid(row=0,
                    column=0,
                    sticky="nsew",
                    padx=16, pady=16)
    Moderation.rowconfigure(0, weight=1)
    Moderation.rowconfigure(1, weight=2)
    Moderation.rowconfigure(2, weight=9**4) # hacky way to make TweetID stay in place
    Moderation.columnconfigure(0, weight=2)
    Moderation.columnconfigure(0, weight=1)

    # Get the tweet that needs to be moderated
    tweet = TA.get_unmoderated_tweet()
    if tweet == None:
        # error message, no tweets to moderate
        error_message = TK.Label(Moderation,
                                 text="No tweets to moderate",
                                 font=("NS sans", 16),
                                 foreground='#333399', background='#FFC917')
        error_message.grid(row=0,
                           column=0,
                           columnspan=2,
                           sticky="nsew",
                           padx=16, pady=16)
        # after a few seconds, destroy the error message and return to login screen
        return
    else:
        # Display the username in a label
        tweet_username = TK.Label(Moderation,
                                  text=tweet[2],
                                  font=("NS sans bold", 16),
                                  anchor="w",
                                  foreground='#333399', background='#FFC917')
        tweet_username.grid(row=0,
                            column=0,
                            columnspan=2,
                            sticky="nsew",
                            padx=16, pady=4
                            )

        # Display the date in a label
        tweet_date = TK.Label(Moderation,
                              text=tweet[3],
                              font=("NS sans bold", 16),
                              foreground='#333399', background='#FFC917')
        tweet_date.grid(row=0,
                        column=3,
                        sticky="nsew",
                        padx=4, pady=4
                        )

        # Display the tweet text in a textbox
        tweet_text = TK.Label(Moderation,
                              text=tweet[4],
                              anchor="nw",
                              font=("NS sans", 16),
                              width=30, height=5,
                              wraplength=366,
                              justify="left",
                              foreground='#333399',
                              borderwidth=2, relief="sunken")
        tweet_text.grid(row=1,
                        column=0,
                        columnspan=2,
                        rowspan=2,
                        sticky="nsew",
                        padx=16, pady=16
                        )

        # Display the date label next to the tweet text
        tweet_station = TK.Label(Moderation,
                                  text=tweet[1],
                                  font=("NS sans", 16),
                                  foreground='#333399', background='#FFC917')
        tweet_station.grid(row=1,
                            column=3,
                            sticky="new",
                            padx=16, pady=16
                            )

        # Display the tweet ID in a label next to the tweet text
        tweet_id = TK.Label(Moderation,
                            text=f"TweetID: {tweet[0]}",
                            font=("NS sans", 16),
                            anchor="n",
                            foreground='#333399', background='#FFC917')
        tweet_id.grid(row=2,
                      column=3,
                      sticky="new",
                      padx=16, pady=16
                      )

        # Display accept button under tweet text disabled
        AcceptButton = TK.Button(Moderation,
                                 text="Accept",
                                 state="disabled",
                                 font=("NS sans bold", 16),
                                 foreground='#333399', background='#ffc300',
                                 relief = "sunken",
                                 command=lambda: accept_tweet(tweet[0],moderator))
        AcceptButton.grid(row=3,
                          column=0,
                          sticky="nsew",
                          padx=16, pady=16)

        # Display deny button next to accept button
        DenyButton = TK.Button(Moderation,
                               text="Deny",
                               font=("NS sans bold", 16),
                               foreground='#333399', background='#FFC917',
                               command=lambda: deny_popup(tweet[0]))
        DenyButton.grid(row=3,
                        column=3,
                        sticky="nsew",
                        padx=16, pady=16)

        MainWindow.geometry("+%d+%d" % (screen_width / 2 - 325, screen_height / 2 - 170))
        MainWindow.after(3000, lambda: AcceptButton.configure(state="normal",foreground='#333399', background='#FFC917',relief="raised"))

# Function to accept a tweet
def accept_tweet(tweet_id, moderator):
    TA.accept_tweet(tweet_id, moderator)
    destroy_layout()
    moderation_screen()

# Function to deny a tweet
def deny_popup(tweetid): #tweet_id
    # create a popup window to confirm the denial
    DenyWindow = TK.Toplevel(MainWindow)
    DenyWindow.title("Deny Tweet")
    DenyWindow.geometry("+%d+%d" % (screen_width / 2 - 325, screen_height / 2 - 170))
    DenyWindow.resizable(False, False)
    DenyWindow.configure(background='#FFC917')

    # Display the deny message in a label
    deny_message = TK.Label(DenyWindow,
                            text="Afwijzing reden:",
                            font=("NS sans", 16),
                            anchor="n",
                            foreground='#333399', background='#FFC917')
    deny_message.grid(row=0,
                      column=0,
                      columnspan=2,
                      sticky="nsew",
                      padx=16, pady=16)

    # display a textbox to enter the deny reason
    deny_reason = TK.Entry(DenyWindow,
                           font=("NS sans", 16),
                           justify="left",
                           foreground='#333399')
    deny_reason.grid(row=1,
                     column=0,
                     columnspan=2,
                     sticky="nsew",
                     padx=16, pady=16)

    # display a button to confirm the denial
    deny_button = TK.Button(DenyWindow,
                            text="Deny Tweet",
                            font=("NS sans bold", 16),
                            foreground='#333399', background='#FFC917',
                            command=lambda: deny_tweet(tweetid, moderator, deny_reason.get(), DenyWindow))
    deny_button.grid(row=2,
                     column=0,
                     columnspan=2,
                     sticky="nsew",
                     padx=16, pady=16)

    #destroy_layout()
    #moderation_screen()

def deny_tweet(tweet_id, moderator, reason, DenyWindow):
    TA.deny_tweet(tweet_id, moderator, reason)
    #destroy deny_popup
    DenyWindow.destroy()
    destroy_layout()
    moderation_screen()

def destroy_layout():
    # Destroy all widgets
    for widget in MainWindow.winfo_children():
        widget.destroy()

login_screen()

MainWindow.configure(background='#FFC917')
MainWindow.protocol("WM_DELETE_WINDOW", con.close())
# Execute the window
MainWindow.mainloop()