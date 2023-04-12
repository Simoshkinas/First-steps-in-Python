# Reading files
# employee_file = open("employees.txt", "r")
# print(employee_file.readable())
# print(employee_file.read())
# employee_file.close()
# employee_file = open("employees.txt", "r")
# print(employee_file.readline())
# employee_file.close()
# employee_file = open("employees.txt", "r")
# print(employee_file.readlines())
# employee_file.close()
# employee_file = open("employees.txt", "r")
# print(employee_file.readlines()[1])
# employee_file.close()
# employee_file = open("employees.txt", "r")
# print(employee_file.readlines()[4])
# employee_file.close()
# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)

# Writing to files

employee_file = open("employees.txt", "w")
employee_file.write("Kelly - Customer service")
employee_file.close()
employee_file = open("employees.txt", "a")
employee_file.write("\nOscar - Accountant")

employee_file.close()
