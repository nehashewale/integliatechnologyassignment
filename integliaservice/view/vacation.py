def create_single_vacation_view(id, employee_id , manager_id, request_created_at, vacation_start_date, vacation_end_date,status):
    return {
        "id" : id, # ENTITY_ID
        "author" : employee_id, # WORKER_ID
        "resolved_by" : manager_id, # MANAGER_ID
        "request_created_at" : request_created_at.strftime("%m/%d/%Y, %H:%M:%S"),
        "vacation_start_date" : vacation_start_date.strftime("%m/%d/%Y, %H:%M:%S"),
        "vacation_end_date" : vacation_end_date.strftime("%m/%d/%Y, %H:%M:%S"),
        "status" : status
    }


def create_multiple_vacation_view(vacations):
    vacation_view = []
    for vacation in vacations:
        resolved_by = ""
        if vacation.resolved_by !=None:
            resolved_by = vacation.resolved_by.employee_id
        vacation_json  = create_single_vacation_view(vacation.id, vacation.author.employee_id , resolved_by , vacation.request_created_at, vacation.vacation_start_date,vacation.vacation_end_date , vacation.status)
        vacation_view.append(vacation_json)
    return vacation_view

