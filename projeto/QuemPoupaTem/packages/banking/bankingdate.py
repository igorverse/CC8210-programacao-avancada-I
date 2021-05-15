"""
When this function is called, it will register the current datetime.
Arguments:
    function without arguments
Return:
    return a string with the current datetime (date and time).
"""


from datetime import datetime

def banking_date():
    
    return datetime.now().strftime("%Y-%m-%d %H:%M")