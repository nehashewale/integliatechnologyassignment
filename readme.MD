
# stack required 
# mysql, python3


# --------------------------------------
# clone git repo

# change user and password accordingly
# create databse integlia
# integliadb/integliadb/settings.py # line number 81 and 82

# virtual enviroment setup
# creating virtual env
python3 -m venv ~/venv-integliate
# activate virtual env 
source ~/venv-integliate/bin/activate
# install packages
cd integliatechnologyassignment/integliadb
pip install -r ../requirements.txt
# migrate to db 
python manage.py makemigrations employee
# creating own package
python setup.py install
# run service
cd integliatechnologyassignment/integliaservice
export DJANGO_SETTINGS_MODULE='integliadb.settings'; export PYTHONPATH=$PWD; 
python service.py


# -------------------------------

# API contracts 


# 1. create employee with manager 

url = "http://127.0.0.1:5000/integliaservice/employee/"

method = POST

body = {
    "name" : "Neha",
    "employee_id" : "NH01",
    "manager_id" : "NE1"
}

# 2. get employee 
url = "http://127.0.0.1:5000/integliaservice/employee/"

method = GET

params = employee_id:NH01


# 3. create vacation 

url = "http://127.0.0.1:5000/integliaservice/vacation/"

method = POST

body = {
    "author" : "NH01",
    "vacation_start_date" : 1630866600000,
    "vacation_end_date" : 1631730600000 
}


# 4. approve / reject vacation 

url = "http://127.0.0.1:5000/integliaservice/vacation/"

method = PUT

body = {
            "id": 2,
            "author": "NH01",
            "resolved_by_id": "NE1",
            "status": "approved"
}

# 5. get all by manager as well as employe by filter vacation 

url = "http://127.0.0.1:5000/vacation/?manager_id=NE1&employee_id=PRA1&status=pending"

method = GET
