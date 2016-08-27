from datetime import datetime
from pytz import timezone

import csv
import pytz


EVENT_START = 'BEGIN:VEVENT'
EVENT_END = 'END:VEVENT'
SUMMARY = 'SUMMARY:'
TYPE = 'GAME'
GAME_TYPE = 'REGULAR'
DATE_START = 'DTSTART:'
LOCATION = 'Yerba Buena Ice Rink'
ADDRESS = '750 Folsom St, San Francisco, CA 94107'
DATE_FORMAT = '%a, %b %d, %Y'
INPUT_DATE_FORMAT = '%Y%m%dT%H%M%SZ'
TIME_FORMAT = '%I:%M %p'

if __name__ == "__main__":
    events = []
    with open('schedule.ics', 'rw') as calendar:
        current_event = None
        for row in calendar:
            row = row.rstrip('\n\r')
            if row.startswith(EVENT_START):
                current_event = {}
                continue
            if row.startswith(SUMMARY):
                row = row.replace(SUMMARY, '')
                team_b, team_a = row.split(" at ")
                current_event.update({
                    'Home': team_a,
                    'Away': team_b,
                })
                continue
            if row.startswith(DATE_START):
                row = row.replace(DATE_START, '')
                date = datetime.strptime(row, INPUT_DATE_FORMAT)
                date = date.replace(tzinfo=pytz.UTC)
                date = date.astimezone(timezone('US/Pacific'))

                current_event['Date'] = date.strftime(DATE_FORMAT)
                current_event['Time'] = date.strftime(TIME_FORMAT)
                continue
            if row.startswith(EVENT_END):
                events.append(current_event)
                continue

    with open('schedule.csv', 'w') as calendar:
        writer = csv.writer(calendar)
        writer.writerow([
            'Type',
            'Game Type',
            'Title (Optional)'
            'Home',
            'Away',
            'Date',
            'Time',
            'Location (Optional)',
            'Address (Optional)',
            'Notes (Optional)'
        ])

        for event in events:
            writer.writerow([
                TYPE,
                GAME_TYPE,
                None,
                event['Home'],
                event['Away'],
                event['Date'],
                event['Time'],
                LOCATION,
                ADDRESS,
                None,
            ])
