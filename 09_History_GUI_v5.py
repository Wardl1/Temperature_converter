# Follows on from 09_History_GUI_v4.py
# Removed all but 4 elements from the list (lines 19-22)
# Then added else statement for list less than 7 elements on lines 90-98
# NOTE the subtle difference between line 88 (whole list) and line 94 which
# uses index values for items in the list.

from tkinter import *
from functools import partial  # To prevent unwanted windows

class Convertor:
    def __init__(self):
        # Formatting variables...
        background_color = "light blue"

        # Initialise list to hold calculation history
        # In later versions list will be populated with user calculations
        self.all_calc_list = ['0 degrees F is -17.8 degrees C',
                                 '0 degrees C is 32 degrees F',
                                 '100 degrees F is 37.8 degrees C',]

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

        # history button (row 1)
        self.history_button = Button(self.convertor_frame, text="History",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):
        background = "#a9ef99"  # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # if users press at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,
                                                           partner))

        # set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent "
                                                           "Calculations. Please use the "
                                                           "export button to create a text "
                                                           "file of all your calculations for"
                                                           "this session",
                                  font="arial 10 italic", wrap=250,
                                  justify=LEFT,
                                  bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here.. (row 2)
        history_string = ""
        if len(calc_history) >=7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)-item-1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item)-1]+"\n"
                self.history_text.config(text="Here is your calculation "
                                              "history. You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="arial 12 bold",
                                     command=partial(self.close_history,
                                                     partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
