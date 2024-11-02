# ICS_server

Is a webserver that hosts ics files. 
It has a post endpoint to post an event 
and to add it to the ics file

## Endpoints

### POST: /add_event/
    
request headers ex:

`X-API-Key: your_secret_api_key`

request body ex: 

```json

{
  "event_name": "Meeting", 
  "start": "2024-10-10T10:00:00", // python datetime
  "duration_h": 2, // float
  "description": "Team sync-up meeting", //Otional
  "location": "Home" //Otional
}

```

To add an api key, add one as an environment var or in a .env file
`API_KEY="your_secret_api_key"`

### GET: /calendar.ics

Returns a ics file