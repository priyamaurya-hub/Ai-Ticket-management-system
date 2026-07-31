from flask import Blueprint, request, jsonify

ticket = Blueprint("ticket", __name__)

@ticket.route("/ticket", methods=["POST"])
def create_ticket():
    data = request.json

    return jsonify({
        "message": "Ticket Created Successfully",
        "data": data
    })