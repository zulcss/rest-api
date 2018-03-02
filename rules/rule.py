from flask import jsonify, request
from flask_restful import Resource

class Rule(Resource):
    def post(self):
        data = request.get_json(force=True)
        ticket = {
            "CaseType": "Infrasturcture NOC Trouble",
            "SubType": "Hazcon",
            "Severity": "Medium",
            "Escelation": "Level 1",
            "SiteName": data.get('device'),
            "Queue": "StormTroopers",
            "title": data.get('name'),
            "description": "Generator Running Fuel Alarm"
        }
        return {
            'ticketRule': ticket
        }
