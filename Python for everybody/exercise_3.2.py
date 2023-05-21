"""
Rewrite your pay computation to give the employee 1.5 times the 
hourly rate for hours worked above 40 hours
"""
hours = input("Enter Hours: ")
rate = input("Enter rate: ")
try:
    f_hours = float(hours)
    f_rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
if f_hours > 40:
    regular_payment = f_hours * f_rate
    overtime_payment = (f_hours - 40) * f_rate * 1.5
    total_payment = regular_payment + overtime_payment
else:
    total_payment = f_hours * f_rate
print("pay: ",total_payment)
