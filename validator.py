# Example of a custom module to be imported
#importing regular expression re
import re

#function Syntax- def functionname(argument):
def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
