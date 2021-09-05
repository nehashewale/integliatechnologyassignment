from flask_restful import Resource
from validator.employee import  validate_user_schema
from flask import request
from dao.employee import get_employee_by_employee_id, create_employee, get_employee_by_id, get_all_employees
from view.employee import create_employee_view_object

class Employee(Resource):
    def post(self):
        # getting body 
        body = request.json

        # validate schema 
        is_valid_schema = validate_user_schema(body)

        if is_valid_schema == False:
            return {"response" : "Invalid Schema"}
        
        employee = get_employee_by_employee_id(body["employee_id"])
        if employee != None:
            return {"response" : "employee already exist"}

        # get manager
        manager_object = None
        if body["manager_id"] != "":
            manager_object = get_employee_by_employee_id(body["manager_id"])
            if manager_object == None:
                return {"response" : "No manager found with manager_id"}
        
        create_employee(body,manager_object)
        return {"reponse" : "Employee created successfully"}

    
    def get(self):
        params = request.args.to_dict()
        if "employee_id" in params:
            employee_id = params['employee_id']
            employee = get_employee_by_employee_id(employee_id)
            if employee == None:
                return {"response":"employee not found"}
            manager = None
            if employee.manager_id != None:
                manager = get_employee_by_id(employee.manager_id)

            employee_json = create_employee_view_object(employee,manager)
            return  {"response" : employee_json}
        else:
            employees = get_all_employees()
            employees_json = []

            for employee in employees:
                manager = None
                if employee.manager_id != None:
                    manager = get_employee_by_id(employee.manager_id)
                employee_json = create_employee_view_object(employee,manager)
                employees_json.append(employee_json)

            return {"response" : employees_json}


