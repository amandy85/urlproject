from django.core.exceptions import ValidationError
from django.core.validators import URLValidator 


def validate_url(value):
    url_validator= URLValidator()
    reg_value =value
    if "http" in reg_value:
        new_value = reg_value
    else:
        new_value= "http://" + value

    try:
        url_validator(new_value)
    except:
        raise ValidationError("Invalid URL for this field")    
    return new_value





def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("not valid because no .com")
    return value