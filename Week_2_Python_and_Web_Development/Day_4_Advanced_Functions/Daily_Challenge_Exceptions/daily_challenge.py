def division_by_zero():
    try: 
        x=5/0
    except ZeroDivisionError:
        x="You can`t divide by zero"
    return x
print(division_by_zero())