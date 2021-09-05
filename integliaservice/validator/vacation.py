from jsonschema import validate


vacation_create_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "author": {"type": "string"},
    "vacation_start_date": {"type": "integer"},
    "vacation_end_date": {"type": "integer"}
    }
}

def validate_vacation_post_schema(body):
    try:
        validate(body,vacation_create_schema)
        return True
    except:
        return False


vacation_edit_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id" : {"type": "string"},
    "author": {"type": "string"},
    "resolved_by_id": {"type": "string"},
    "status": {"type": "string"}
    }
}

def validate_vacation_put_schema(body):
    try:
        validate(body,vacation_create_schema)
        return True
    except:
        return False


