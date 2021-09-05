
def create_employee_view_object(employee,manager):
    manager_employee_id = ""
    manager_name = ""
    
    if manager != None:
        manager_employee_id = manager.employee_id
        manager_name = manager.name

    return {
        "name": employee.name,
        "employee_id": employee.employee_id,
        "manager_employee_id": manager_employee_id,
        "manager_name" : manager_name
        }