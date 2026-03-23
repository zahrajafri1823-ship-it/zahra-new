employees = {}
employees["Amit"] = 25000
employees["Neha"] = 30000
employees["Rohit"] = 28000
for name in employees:
    employees[name] += 2000
print("Updated Salaries:")
for name in employees:
    print(name, ":", employees[name])
