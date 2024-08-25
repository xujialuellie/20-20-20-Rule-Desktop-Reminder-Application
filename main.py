import tkinter
import time
import pygame

# Create a tkinter window
window = tkinter.Tk()
window.title("Desktop Reminder Application")
window.geometry("600x300")

# Create a function to show the start of the application
def start():
    
    # Check if any labels or buttons from other pages exist before showing the start page, and destroy them if they exist
    labels_to_destroy = ['countdown_label', 'stop_button', 'reminder_label', 'reminder_countdown_label', 'stop_music_button', 'go_back_button', 'focus_label']
    for label_name in labels_to_destroy:
        if label_name in globals():
            globals()[label_name].destroy()

    global welcome_label  # Declare welcome_label as a global variable
    global start_button  # Declare start_button as a global variable

    # Create a welcome label
    welcome_label = tkinter.Label(window, text="Welcome to the Desktop Reminder Application", font=("Courier", 20))
    welcome_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    # Create a start button
    start_button = tkinter.Button(window, text="Start", font=("Courier", 20), fg="green", relief="raised", bd=5, command=countdown)
    start_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    window.update()

# Create a function to show the countdown part of the application
def countdown():

    global focus_label  # Declare focus_label as a global variable
    global countdown_label  # Declare countdown_label as a global variable
    global stop_button # Declare as a global variable

    # Hide the welcome label and start button
    welcome_label.destroy()
    start_button.place_forget()

    # Create a focus label
    focus_label = tkinter.Label(window, text="Focus on your work for 20 minutes.", font=("Courier", 20))
    focus_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    # Create a countdown timer that counts down 20 minutes
    def update_countdown():
        remaining_time = end_time - time.time()
        countdown_label.config(text="Remaining Time: " + str(int(remaining_time // 60)) + " minutes " + str(int(remaining_time % 60)) + " seconds")
        if remaining_time > 0:
            window.after(100, update_countdown)
        else:
            reminder()

    start_time = time.time()
    end_time = start_time + 20
    countdown_label = tkinter.Label(window, text="", font=("Courier", 15))
    countdown_label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    # Create a Stop button to stop the countdown and go back to the start page
    stop_button = tkinter.Button(window, text="Stop", font=("Courier", 20), fg="red", relief="raised", bd=5, command=start)
    stop_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    update_countdown()

# Create a function to show the reminder part of the application
def reminder():

    global reminder_label  # Declare as a global variable
    global reminder_countdown_label  # Declare as a global variable
    global stop_music_button  # Declare as a global variable
    global go_back_button  # Declare as a global variable

    # Hide the stop button, focus label, and countdown label
    stop_button.place_forget()
    focus_label.destroy()
    countdown_label.destroy()

    # Make sure the window pop up on top of all other windows to remind the user
    window.attributes("-topmost", True)

    # Play a sound to remind the user
    pygame.mixer.init()
    pygame.mixer.music.load("reminder_sound.wav")
    pygame.mixer.music.play(-1)  # Set the loop parameter to -1 to play the sound indefinitely

    # Make sure the sound stops after 20 seconds relaxing time
    window.after(20000, pygame.mixer.music.stop)

    # Create a reminder message
    reminder_label = tkinter.Label(window, text="Give your eyes a 20-second break:\nFocus on something 20 feet away\nto relax your eye muscles.", font=("Courier", 20))
    reminder_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    # Give the reminder label a background color and a better design
    reminder_label.configure(bg="#EDF4F2", fg="#31473A", relief="raised", bd=5)

    window.update()
    
    # Create a countdown timer that counts down 20 minutes
    def update_relaxing_countdown():
        remaining_time = end_time - time.time()
        reminder_countdown_label.config(text="Relaxing Time: " + str(int(remaining_time)) + " seconds")
        if remaining_time > 0:
            window.after(100, update_relaxing_countdown)
        else:
            start()

    # Create a 20-second reminder countdown timer under the reminder label
    start_time = time.time()
    end_time = start_time + 20
    reminder_countdown_label = tkinter.Label(window, text="", font=("Courier", 15))
    reminder_countdown_label.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    
    # Create a button to let the user stop the music manually
    stop_music_button = tkinter.Button(window, text="Stop Music", font=("Courier", 15), command=pygame.mixer.music.stop)
    stop_music_button.place(relx=0.4, rely=0.9, anchor=tkinter.CENTER)

    # Create a button to let the user go back to the start page
    go_back_button = tkinter.Button(window, text="Go Back", font=("Courier", 15), command=lambda: [start(), pygame.mixer.music.stop()])
    go_back_button.place(relx=0.6, rely=0.9, anchor=tkinter.CENTER)

    update_relaxing_countdown()

# Start the application by showing the beginning
start()

# Prevent the window from being resized
window.resizable(0, 0)

# Start the tkinter event loop
window.mainloop()
