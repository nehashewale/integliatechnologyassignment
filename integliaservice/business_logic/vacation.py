
from dao.employee import get_employee_by_employee_id
from dao.vacation import get_all_vacations_by_employee_id
from constant.vacation import max_holiday_limit
from utils.time import convert_to_date

def update_vacation_status(vacation,resolved_by_id, status):
    manager = get_employee_by_employee_id(resolved_by_id)
    if manager == None:
        return {"response" : "Not valid manager"}
    
    vacation.status = status
    vacation.resolved_by = manager
    vacation.save()

def calculate_remaining_leaves(vacations):
    total_vacation_days_used = 0
    for vacation in vacations: 
        vacation_difference = vacation.vacation_end_date - vacation.vacation_start_date
        total_vacation_days_used = total_vacation_days_used +  vacation_difference.days
    return total_vacation_days_used

def is_eligible_for_leaves(start_date, end_date, employee_id):

    request_leave = convert_to_date(end_date) - convert_to_date(start_date)
    vacations = get_all_vacations_by_employee_id(employee_id)
    remaining_days = calculate_remaining_leaves(vacations)
    if (max_holiday_limit - remaining_days) >= request_leave.days:
        return True

    return False



# test cases 
if __name__ == "__main__":
    start_time = 1630866600000
    end_time = 1631730600000
    is_valid = is_eligible_for_leaves(start_time, end_time, "ABC")
    print(is_valid)