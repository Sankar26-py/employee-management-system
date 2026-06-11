from employees.models import Employee


# 43. raw()
Employee.objects.raw("""
SELECT *
FROM employees_employee
WHERE salary > 100000
""")


# 44. iterator()
for emp in Employee.objects.iterator():
    print(emp.name)


# 45. union()
# 46. intersection()
# 47. difference()

high_salary = Employee.objects.filter(
    salary__gt=100000
)

female = Employee.objects.filter(
    gender="female"
)

high_salary.union(female)

high_salary.intersection(female)

high_salary.difference(female)


# 48. db_manager()
Employee.objects.db_manager(
    "default"
).count()


# 49. bulk_update()
employees = list(
    Employee.objects.all()[:10]
)

for emp in employees:
    emp.salary += 1000

Employee.objects.bulk_update(
    employees,
    ["salary"]
)


# 50. explain()
Employee.objects.filter(
    salary__gt=100000
).explain()