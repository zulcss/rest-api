from flask import jsonify, request
from flask_restful import Resource

class Ticket(Resource):
    def post(self):
        data = request.get_json(force=True)
        ticket = {
            "CaseType": "Infrasturcture NOC Trouble",
            "Escelation": data.get('Escelation'),
            "Queue": data.get('Queue'),
            "Severity": data.get('Severity'),
            "SiteName": data.get('SiteName'),
            "SubType": "Hazcon",
            "TicketId": 4,
            "description": data.get('description'),
            "title": data.get('title')
        }

        return {
            'task': ticket
        }
