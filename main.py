from config import API_KEY, API_KEY_NAME
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.responses import PlainTextResponse
from calendarTracker import CalendarTracker, EventRequest


calendar_tracker = CalendarTracker()

app = FastAPI()

api_key_header = APIKeyHeader(name=API_KEY_NAME)


# Dependency to check for API key
async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")


# Add an event to the calendar (POST request with JSON body)
@app.post("/add_event/")
async def add_calendar_event(event: EventRequest, api_key: str = Depends(verify_api_key)):
    """
    Add an event to the ICS feed.
    :param event: EventRequest model with event_name, start, duration, and description
    :param api_key: API key for authentication
    :return: Success message
    """
    try:
        # Parse the start time to ensure it's valid
        calendar_tracker.add_event(event)
        print(event)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid start time format. Use 'YYYY-MM-DDTHH:MM'")

    # Add the event using the calendar service

    return {"message": "Event added successfully"}


# Return the ICS calendar feed
@app.get("/calendar.ics", response_class=PlainTextResponse)
def get_ics_feed():
    """
    Return the calendar feed as an ICS file.
    """
    ics_content = calendar_tracker.get_string_cal()
    return ics_content


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
