
import time
from datetime import datetime
def get_iso_date(date):
    try:
        return datetime.strptime(date, '%d-%B-%Y').strftime('%Y-%m-%d')
    except:
        return


def get_utc_ms_time(date):
    try:
        return int(time.mktime(date.timetuple())) * 1000

    except:
        return ''

def convert_to_date(millis):
    return datetime.fromtimestamp(millis/1000.0)