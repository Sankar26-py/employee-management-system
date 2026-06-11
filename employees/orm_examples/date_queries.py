from employees.models import Employee
from tasks.models import Task


def run():

    print("\n========== DATE & DATETIME QUERIES ==========")

    # 51. dates() Returns a list of date objects extracted from a DateField (or DateTimeField) of your model, filtering for distinct dates.
    # Returns available dates truncated to year.
    print("\n51. dates()")

    years = Employee.objects.dates("joining_date","year")

    for year in years:

        print(year)

    # 52. datetimes() Similar to dates(), but returns datetime objects. It’s useful for grouping or displaying times along with dates.
    # Returns available datetimes truncated to month.
    print("\n52. datetimes()")

    months = Task.objects.datetimes("created_at","month")

    for month in months:

        print(month)