
import django;django.setup()

from integliadb.employee.models import Vacation
from datetime import datetime
from django.db.models import Q
from utils.time import convert_to_date


def create_vacation(vacation_start_date, vacation_end_date, employee):
    vacation = Vacation.objects.create(
        status = "pending",
        vacation_start_date = convert_to_date(vacation_start_date),
        vacation_end_date = convert_to_date(vacation_end_date),
        author = employee
        )
    return vacation


def get_all_vacations_by_employee(employee):
    vacations = Vacation.objects.filter(author=employee)
    return vacations

def get_all_vacations_by_manager(manager):
    vacations = Vacation.objects.filter(author__manager=manager)
    return vacations

def get_all_vacations_by_manager_and_status(manager,statuses):
    vacations = Vacation.objects.filter(author__manager=manager,status__in=statuses)
    return vacations


def get_all_vacations_by_manager_employee_and_status(manager,employee_id,statuses):
    vacations = Vacation.objects.filter(author__employee_id=employee_id,author__manager=manager,status__in=statuses)
    return vacations

def get_vacation_by_vacation_id(id):
    try:
        vacation = Vacation.objects.get(id=id)
        return vacation
    except:
        return None


def get_vacation_by_vacation_id_and_manager_id(id,manager_id):
    try:
        vacation = Vacation.objects.get(id=id,author__manager__employee_id=manager_id)
        return vacation
    except:
        return None

def get_all_vacations_by_employee_id_and_status(employee_id,statuses):
    vacations = Vacation.objects.filter(author__employee_id=employee_id,status__in=statuses)
    return vacations

    
def get_all_vacations_by_employee_id(employee_id):
    vacations = Vacation.objects.filter(author__employee_id=employee_id)
    return vacations