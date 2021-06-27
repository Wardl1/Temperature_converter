from tkinter import *


class Convertor:
    def __init__(self):
        # Formatting variables...
        background_color = "light blue"

        # Convertor Main Screen GUI..
        self.convertor_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.convertor_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_convertor_label = Label(self.convertor_frame,
                                          text="Temperature Convertor",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # Help button (row 1)
        self.help_button = Button(self.convertor_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self):
        background = "orange"


    # set up GUI Frame

    # Set up Help heading (row 0)

    # Help text (label, row 1)

    # Dismiss button (row 2)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
