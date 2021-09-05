from flask import Flask
from flask_restful import Resource, Api
from handler.ping import Ping
from handler.employee import Employee
from handler.vacation import Vacation


from flask import request 


app = Flask(__name__)
api = Api(app)
api.add_resource(Ping, '/integliaservice/ping/')
api.add_resource(Employee, '/integliaservice/employee/')
api.add_resource(Vacation, '/integliaservice/vacation/')


if __name__ == '__main__':
    app.run(debug=True)