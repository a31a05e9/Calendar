import tkinter as tk
from tkinter import messagebox
from calendar import monthrange, month_name
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calendar")

        # Initialize current year and month
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the calendar
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack(padx=10, pady=10)

        # Create a frame for the dropdowns
        self.controls_frame = tk.Frame(self.calendar_frame)
        self.controls_frame.grid(row=0, column=0, columnspan=7, pady=5)

        # Create month dropdown
        self.month_var = tk.StringVar(value=month_name[self.current_month])
        self.month_menu = tk.OptionMenu(self.controls_frame, self.month_var, *month_name[1:])
        self.month_menu.pack(side=tk.LEFT, padx=5)

        # Create year dropdown
        self.year_var = tk.StringVar(value=str(self.current_year))
        self.year_menu = tk.OptionMenu(self.controls_frame, self.year_var, *[str(year) for year in range(self.current_year - 10, self.current_year + 11)])
        self.year_menu.pack(side=tk.LEFT, padx=5)

        # Bind dropdown selection changes to update the calendar
        self.month_var.trace('w', self.update_calendar_from_dropdowns)
        self.year_var.trace('w', self.update_calendar_from_dropdowns)

        # Create the days of the week labels
        self.days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        self.days_labels = []
        for i, day in enumerate(self.days_of_week):
            label = tk.Label(self.calendar_frame, text=day, font=('Arial', 12, 'bold'))
            label.grid(row=1, column=i, padx=5, pady=5)
            self.days_labels.append(label)

        # Create a grid for the calendar days
        self.days_buttons = []
        for i in range(6):
            row_buttons = []
            for j in range(7):
                button = tk.Button(self.calendar_frame, text="", width=4, height=2, command=lambda d=i*7+j: self.show_day(d))
                button.grid(row=i+2, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.days_buttons.append(row_buttons)

        # Initial calendar update
        self.update_calendar()

    def update_calendar(self):
        self.current_month = list(month_name).index(self.month_var.get())
        self.current_year = int(self.year_var.get())

        # Update the header with current month and year
        self.month_year_label = tk.Label(self.controls_frame, text=f"{month_name[self.current_month]} {self.current_year}", font=('Arial', 16))
        self.month_year_label.pack(side=tk.LEFT, padx=10, pady=5)

        # Get the first day of the month and number of days in the month
        first_day_of_month = datetime(self.current_year, self.current_month, 1)
        last_day_of_month = monthrange(self.current_year, self.current_month)[1]

        # Clear previous days
        for row in self.days_buttons:
            for button in row:
                button.config(text="", state=tk.NORMAL)

        # Fill in the days of the month
        for day in range(1, last_day_of_month + 1):
            row = (first_day_of_month.weekday() + day) // 7 + 2
            col = (first_day_of_month.weekday() + day) % 7
            self.days_buttons[row - 2][col].config(text=str(day))

    def update_calendar_from_dropdowns(self, *args):
        self.update_calendar()

    def show_day(self, day_index):
        row = day_index // 7
        col = day_index % 7
        day_text = self.days_buttons[row][col].cget("text")
        if day_text:
            messagebox.showinfo("Day Info", f"Selected Day: {day_text} {month_name[self.current_month]} {self.current_year}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
