from django.db.models import (F,Sum,Window
)

from django.db.models.functions import (
    Rank,
    RowNumber
)

from employees.models import Employee


def run():

    print("\n========== ADVANCED EXPRESSIONS & WINDOW FUNCTIONS ==========")

    # 53. alias()Creates temporary names (aliases) for expressions in a queryset. 
    # This helps when you want to reuse the same calculation or annotate multiple times.
    # Creates a reusable SQL expression.
    print("\n53. alias()")

    employees = (Employee.objects.alias(annual_salary=F("salary") * 12).filter(annual_salary__gt=1200000))

    for employee in employees[:5]:

        print(
            employee.name,
            employee.salary
        )

    # 54. update_fields When saving a model instance, you can tell Django to update only specific fields.
    # Updates only specified fields.
    print("\n54. update_fields")

    employee = Employee.objects.first()

    if employee:

        old_salary = employee.salary

        employee.salary += 500

        employee.save(update_fields=["salary"])

        print(f"{employee.name}: "f"{old_salary} -> {employee.salary}")

    # 55. Rank()
    # What it does:
    # Enables use of SQL window (analytic) functions. These can compute rankings, running totals,
    # moving averages, etc., across a set of rows.

    # When to use:
    # When you need to perform analytic queries (e.g., ranking books by sales) without raw SQL.
    # Assigns ranking with gaps.
    print("\n55. Rank()")

    employees = Employee.objects.annotate(salary_rank=Window(expression=Rank(),order_by=F("salary").desc()))

    for employee in employees[:5]:

        print(
            employee.name,
            employee.salary,
            employee.salary_rank
        )

    # 56. RowNumber()
    # Assigns sequential row numbers.
    print("\n56. RowNumber()")

    employees = Employee.objects.annotate(
        row_number=Window(
            expression=RowNumber(),
            order_by=F("salary").desc()
            )
        )

    for employee in employees[:5]:

        print(employee.name,employee.salary,employee.row_number)

    # 57. Running Total
    # Calculates cumulative salary total.
    print("\n57. Running Total")

    employees = Employee.objects.annotate(
        running_salary=Window(
            expression=Sum("salary"),
            order_by="joining_date"
        )
    )

    for employee in employees[:5]:

        print(employee.name,employee.salary,employee.running_salary)