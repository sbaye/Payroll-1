
# payroll assignment 1
employee = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
employeeName = input("employee: ")
salary = float(input("employee salary: "))
hoursWorked = float(input("Please enter hours worked: ", ))
payRate = float(input("Please enter your pay rate: $", ))
regularPay = float(hoursWorked * payRate)
overTimeHours = float(hoursWorked - 40.00)
overTimeRate = float(payRate * 1.5)
overTimePay = float(overTimeHours * overTimeRate)
grossPay = float(regularPay + overTimePay)
fedTax = (0.1 * salary)
stateTax = (0.06 * salary)
FICA = (0.03 * salary)
netPay = salary - fedTax - stateTax - FICA
if hoursWorked <= 40:
    print("employee Name: ", employeeName)
    print("Hours Worked: ", hoursWorked)
    print("Pay Rate: $", payRate)
    print("Regular Pay: $", regularPay)
    print("Gross Pay: $", grossPay)
    print("Fed Tax: $", fedTax)
    print("State Tax: $", stateTax)
    print("FICA: $", FICA)
    print("Net Pay: $", netPay)
elif hoursWorked > 40:
    overTimeHours = float(hoursWorked - 40.00)
    overTimeRate = float(payRate * 1.5)
    overTimePay = float(overTimeHours * overTimeRate)
    print("employee Name: ", employeeName)
    print("Hours Worked: ", hoursWorked)
    print("Pay Rate: $", payRate)
    print("Regular Pay: $", regularPay)
    print("Overtime Pay: $", overTimePay)
    print("Gross Pay: $", grossPay)
    print("Fed Tax: $", fedTax)
    print("State Tax: $", stateTax)
    print("FICA: $", FICA)
    print("Net Pay: $", netPay)



