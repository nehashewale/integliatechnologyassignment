import django;django.setup()

from integliadb.employee.models import Employee

def get_employee_by_employee_id(employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
        return employee
    except Exception as e:
        return None

def get_employee_by_id(id):
    try:
        employee = Employee.objects.get(id=id)
        return employee
    except Exception as e:
        return None


def create_employee(employee_data,manager_object):
    
    employee = Employee.objects.create(
        name = employee_data["name"],
        employee_id = employee_data["employee_id"],
        manager = manager_object,
        )
    return employee



def get_all_employees():
    employees = Employee.objects.all()
    return employees 


