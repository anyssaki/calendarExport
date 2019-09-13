### calendarExport
Attempting to export ASU's composite sports calendar to Google Calendar with Python and Selenium.  

# The Situation
Currently, ASU does not provide an option to import calendar events to a personal calendar easily.  The probable solution for most individuals would be to rely on social media reminders and/or manually add the calendar events.

# Trial #1
Initially, I tried to export the calendar data to Excel and Power BI with the built-in web scraping tools.  Through research, I realized that ASU is utilizing the knockout.js framework.  From what I understand, this Model-View-View model pattern stores the original data separately from the user interface.  Therefore, the client is unable to retrieve the data directly as the aforementioned web scraping tools do.

# Trial #2
The task sequence I imagined to take place had been the following:
1. Using Google Chrome, go to https://thesundevils.com/calendar.aspx
2. Change the location selection from "All Games" to "Home"
3. Navigate through the datepicker starting with "today" until a date has a home sport event
3. Identify and store the event values as separate variables
4. Using the Google Calendar API, create a calendar event using the variables as inputs
5. Repeat the process for the entire month

However, I came across an issue where all dates within the same month return the same result - that month's calendar view of events.  Since the datepicker does not work, I needed to come up with another plan.
