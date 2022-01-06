basic_salary = int(input("enter the basic salary: "))
DA = 40 * 0.01 * (basic_salary)
HRA = 20 * 0.01 * (basic_salary)
PF = 11 * 0.01 * (basic_salary)
gross_salary = basic_salary + DA + HRA - PF
print("gross_salary is:", gross_salary)


