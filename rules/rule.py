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
    
    def get(self, site):
        return {
            "ticket": [
                {
                    "CLLI": site,
                    "CaseType": "Infrasturcture NOC Trouble",
                    "Escelation": "Level 1",
                    "Owner": "Jones, Bob",
                    "Queue": "StormTroopers",
                    "Severity": "Medium",
                    "SiteName": site,
                    "SubType": "Hazcon",
                    "TicketId": 2,
                    "description": "Generator Running",
                    "title": "AC-GEN RUN"
                }
        ]
    }
