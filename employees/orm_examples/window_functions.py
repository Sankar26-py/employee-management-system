from django.db.models import (
    F,
    Sum,
    Window
)

from django.db.models.functions import (
    Rank,
    RowNumber
)

from employees.models import Employee


# 53. alias()
Employee.objects.alias(
    annual_salary=F("salary") * 12
).filter(
    annual_salary__gt=1200000
)


# 54. update_fields
employee = Employee.objects.first()

employee.salary += 500

employee.save(
    update_fields=["salary"]
)


# 55. Rank
Employee.objects.annotate(
    salary_rank=Window(
        expression=Rank(),
        order_by=F("salary").desc()
    )
)


# 56. RowNumber
Employee.objects.annotate(
    row_number=Window(
        expression=RowNumber(),
        order_by=F("salary").desc()
    )
)


# 57. Running Total
Employee.objects.annotate(
    running_salary=Window(
        expression=Sum("salary"),
        order_by="joining_date"
    )
)