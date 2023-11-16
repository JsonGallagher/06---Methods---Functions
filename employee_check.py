# Employee work hours
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

def employee_check(work_hours):
    # Init vars to track the max hours worked + the corresponding employee
    current_max = 0
    employee_of_the_month = ''

    # Iterate through each employee + their worked hours
    for employee, hours in work_hours:
        # Update the employee of the month if current employee has worked more hours
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee

    # Return a tuple with employee of the month + their worked hours
    return (employee_of_the_month, current_max)

# Call the function with the work_hours list + store the result
top_employee, hours = employee_check(work_hours)

# Print the employee of the month + their worked hours
print(f"The employee of the month is {top_employee}, who worked {hours} hours.")
