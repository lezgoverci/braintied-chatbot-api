from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime

# Scopes required to access and modify calendar events
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    """Authenticate to Google API and return service object."""
    flow = InstalledAppFlow.from_client_secrets_file('./credentials.json', SCOPES)
    creds = flow.run_local_server(port=5050)
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_event(service, event):
    """Create an event in the user's calendar."""
    event_result = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event_result.get('htmlLink')}")

def main():
    service = authenticate_google()

    # Define the event details
    event = {
    'summary': 'Midnight Celebration',
    'location': 'Manila, Philippines',
    'description': 'Celebrating at midnight.',
    'start': {
        'dateTime': '2023-12-25T00:00:00+08:00',  # 12 midnight on December 25, 2023, Philippine Time
        'timeZone': 'Asia/Manila',
    },
    'end': {
        'dateTime': '2023-12-25T01:00:00+08:00',  # 1 AM on December 25, 2023, Philippine Time
        'timeZone': 'Asia/Manila',
    },
    }


    create_event(service, event)

if __name__ == '__main__':
    main()
