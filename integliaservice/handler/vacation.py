from flask_restful import Resource
from validator.vacation import  validate_vacation_post_schema, validate_vacation_put_schema
from flask import request
from dao.vacation import create_vacation, get_all_vacations_by_manager_and_status, get_vacation_by_vacation_id_and_manager_id, get_all_vacations_by_employee_id_and_status, get_all_vacations_by_employee_id,get_all_vacations_by_manager, get_all_vacations_by_manager_employee_and_status
from dao.employee import get_employee_by_employee_id
from view.vacation import create_multiple_vacation_view
from business_logic.vacation import update_vacation_status, calculate_remaining_leaves, is_eligible_for_leaves
from constant.vacation import max_holiday_limit
class Vacation(Resource):
    def post(self):
        # getting body 
        body = request.json

        # validate schema 
        is_valid_schema = validate_vacation_post_schema(body)

        if is_valid_schema == False:
            return {"response" : "Invalid Schema"}
        
        employee = get_employee_by_employee_id(body["author"])
        if employee == None:
            return {"response" : "Not valid employee"}
        # validation for remaining leaves
        is_valid = is_eligible_for_leaves(body["vacation_start_date"], body["vacation_end_date"], employee.employee_id)
        if is_valid == False:
            return {"response" : "leave limit exhausted"}
        # create vacation
        create_vacation(body["vacation_start_date"], body["vacation_end_date"], employee)
        return {"reponse" : "Vacation created successfully"}

    def put(self):
        # getting body 
        body = request.json

        # validate schema 
        is_valid_schema = validate_vacation_put_schema(body)

        if is_valid_schema == False:
            return {"response" : "Invalid Schema"}

        if body["status"] not in ["approved", "rejected"]:
            return {"response" : "not a valid status"} 
    

        vacation = get_vacation_by_vacation_id_and_manager_id(body["id"], body["resolved_by_id"])
        if vacation == None:
            return {"response" : "vacation does not exist"}
        
        if vacation.status != "pending":
            return {"response" : "vacation already approved or rejected"}

        update_vacation_status(vacation,body["resolved_by_id"], body["status"] )

        return {"reponse" : "Vacation updated successfully"}

    def get(self): 
        params = request.args.to_dict()
        status = []
        if "status" in params:
            status = params["status"].split(",")
        if "manager_id" in params:
            employee_id = ""
            if "employee_id" in params:
                employee_id = params["employee_id"]

            manager_id = params['manager_id']
            manager = get_employee_by_employee_id(manager_id)
            if manager == None:
                return {"response":"manager not found"}
            vacations = []
            if employee_id == "":
                vacations = get_all_vacations_by_manager_and_status(manager,status)
            else:
                vacations = get_all_vacations_by_manager_employee_and_status(manager, employee_id,status)
            vacation_json = create_multiple_vacation_view(vacations)
            vacations = get_all_vacations_by_manager(manager)
            return {"response" : { "vacations" : vacation_json}}

        if "employee_id" in params:
            vacations = get_all_vacations_by_employee_id_and_status(params['employee_id'], status)
            vacation_json = create_multiple_vacation_view(vacations)
            vacations = get_all_vacations_by_employee_id(params['employee_id'])
            remaining_days = calculate_remaining_leaves(vacations)
            return {"response" : { "vacations" : vacation_json}, "remaining_leaves" : str(max_holiday_limit - remaining_days)+ " days"}
        
    