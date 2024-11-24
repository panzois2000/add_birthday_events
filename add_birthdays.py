from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import datetime

# Authenticate and initialize the Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']
def authenticate_google_calendar():
    creds = None
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('calendar.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

# Function to add birthdays
def add_birthday(calendar_service, name, birthday_date):
    event = {
        'summary': f"🎂 {name}'s Birthday",
        'description': f"{name}'s birthday celebration!",
        'start': {'date': birthday_date},
        'end': {'date': birthday_date},
    }
    calendar_service.events().insert(calendarId='primary', body=event).execute()

# Define birthdays add them as the first example
birthdays = [
    ("John Doe", "2024-01-01"),
	....
]

# Main execution
def main():
    service = authenticate_google_calendar()
    for name, date in birthdays:
        add_birthday(service, name, date)
    print("Birthdays have been added to your Google Calendar.")

if __name__ == '__main__':
    main()
