# Event Management API (Flask Full CRUD Lab)

A RESTful API built with Flask for managing events. Data is stored in an in-memory list of `Event` objects, so it resets when the server restarts.

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip install flask pytest
python3 app.py     # http://localhost:5000
pytest             # run tests
```

## Routes
| Method | Route          | Description             | Success | Errors   |
|--------|----------------|-------------------------|---------|----------|
| POST   | `/events`      | Create a new event      | 201     | 400      |
| PATCH  | `/events/<id>` | Update an event's title | 200     | 400, 404 |
| DELETE | `/events/<id>` | Delete an event         | 204     | 404      |

## Examples
- `POST /events` with `{ "title": "Hackathon" }` → `201` `{ "id": 3, "title": "Hackathon" }`
- `PATCH /events/1` with `{ "title": "Hackathon 2025" }` → `200` `{ "id": 1, "title": "Hackathon 2025" }`
- `DELETE /events/2` → `204 No Content`
- Missing title → `400` `{ "error": "Title is required" }`
- Unknown id → `404` `{ "error": "Event with id 99 not found" }`