from ics import Calendar, Event
from datetime import datetime, timedelta
from pydantic import BaseModel, field_validator


# Pydantic model to parse the incoming event data
class EventRequest(BaseModel):
    event_name: str
    start: datetime  # Expecting ISO 8601 format (e.g., 'YYYY-MM-DDTHH:MM')
    duration_h: float  # Duration in hours
    description: str = ""  # Optional event description
    location: str = ""

    @field_validator("start", mode="before")
    def make_naive(cls, v):
        # Strip timezone if present
        if isinstance(v, datetime) and v.tzinfo:
            return v.replace(tzinfo=None)
        return v


class CalendarTracker:
    def __init__(self):
        self.calendar = Calendar()

    def add_event(self, requested_event: EventRequest):

        event = Event()
        event.name = requested_event.event_name
        event.begin = requested_event.start
        event.end = requested_event.start + timedelta(hours=requested_event.duration_h)
        event.description = requested_event.description
        event.location = requested_event.location

        # Add the event to the calendar
        self.calendar.events.add(event)

    def get_string_cal(self):
        return str(self.calendar)


