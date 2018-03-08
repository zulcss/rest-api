from flask import Flask
from flask_restful import Api

from rules.ticket import Ticket
from rules.rule import Rule

app = Flask(__name__)
api = Api(app)

api.add_resource(Rule, '/serviceAssurance/v1/ticketBySite/<site>',
        '/serviceAssurance/v1/ticketBySite/')
api.add_resource(Ticket, '/serviceAssurance/v1/tickets')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
