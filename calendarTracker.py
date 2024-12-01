from ics import Calendar, Event
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel, field_validator
import pytz


# Pydantic model to parse the incoming event data
class EventRequest(BaseModel):
    event_name: str
    start: datetime  # Expecting ISO 8601 format (e.g., 'YYYY-MM-DDTHH:MM')
    duration_h: float  # Duration in hours
    description: str = ""  # Optional event description
    location: str = ""

    @field_validator("start", mode="before")
    def add_utc_plus_one(cls, v):

        if isinstance(v, str):
            v = datetime.fromisoformat(v)

        # if isinstance(v, datetime):
        #     if v.tzinfo is None:
        #         return v.replace(tzinfo=timezone(timedelta(hours=utc_add)))
        #     return v.astimezone(timezone(timedelta(hours=utc_add)))

        raise ValueError("Invalid format for 'start'. Expected ISO 8601 datetime.")


class CalendarTracker:
    def __init__(self, utc: int):
        self.calendar = Calendar()


    def add_event(self, requested_event: EventRequest):

        start_date = requested_event.start.replace(tzinfo=pytz.timezone("Europe/Stockholm"))
        end_date = requested_event.start.replace(tzinfo=pytz.timezone("Europe/Stockholm")) + timedelta(hours=requested_event.duration_h)

        event = Event()
        event.name = requested_event.event_name
        event.begin = start_date
        event.end = end_date
        event.description = requested_event.description
        event.location = requested_event.location

        # Add the event to the calendar
        self.calendar.events.add(event)

    def get_string_cal(self):
        return str(self.calendar)


