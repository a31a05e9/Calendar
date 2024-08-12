# Simple Calendar App

## Overview

This is a simple calendar application built using Python's Tkinter library. The app displays a calendar for a selected month and year, and allows users to view details of a selected day. The calendar is interactive, letting users choose different months and years from dropdown menus.

## Features

- View and interact with a calendar of any month and year.
- Select different months and years using dropdown menus.
- Click on any day to see a pop-up with the selected date information.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Code Explanation
- CalendarApp Class: The main class that initializes the Tkinter window, creates the calendar UI, and handles user interactions.
- create_widgets Method: Sets up the calendar UI, including dropdowns for month and year selection and a grid for displaying days.
- update_calendar Method: Updates the calendar to reflect the selected month and year.
- update_calendar_from_dropdowns Method: Refreshes the calendar when month or year is changed using dropdowns.
- show_day Method: Displays a message box with information about the selected day.
## Usage
- Change Month and Year: Use the dropdown menus to select different months and years. The calendar will update automatically.
- Select a Day: Click on any day in the calendar to view its details in a pop-up message box.
