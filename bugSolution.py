def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle the error in another appropriate way

result = my_function(10, 0) # this will return 0
result2 = my_function(10,2) # this will return 5.0