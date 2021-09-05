from jsonschema import validate


schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "employee_id": {"type": "string"},
    "manager_id": {"type": "string"}
    }
}

def validate_user_schema(body):
    try:
        validate(body,schema)
        return True
    except:
        return False