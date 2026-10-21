from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


# Helper: find an event by its id (avoids repeating the same loop in every route)
def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None


# Helper: next available id (max existing id + 1, or 1 if the list is empty)
def next_id():
    return max((event.id for event in events), default=0) + 1


# POST /events - Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # silent=True returns None instead of raising if the body isn't valid JSON
    data = request.get_json(silent=True)

    # Validate input: title is required and must not be blank
    if not data or not str(data.get("title", "")).strip():
        return jsonify({"error": "Title is required"}), 400

    new_event = Event(next_id(), data["title"])
    events.append(new_event)

    # 201 Created for a successful POST
    return jsonify(new_event.to_dict()), 201


# PATCH /events/<id> - Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404

    data = request.get_json(silent=True)
    if not data or not str(data.get("title", "")).strip():
        return jsonify({"error": "Title is required"}), 400

    event.title = data["title"]

    # 200 OK with the updated event
    return jsonify(event.to_dict()), 200


# DELETE /events/<id> - Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404

    events.remove(event)

    # 204 No Content: success, nothing to send back
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)