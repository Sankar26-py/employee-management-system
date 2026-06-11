from employees.models import Employee


def run():

    print("\n========== ADVANCED QUERYSET METHODS ==========")

    # 43. raw() Execute raw SQL and return model instances.
    print("\n43. raw()")

    employees = Employee.objects.raw("""
                                SELECT *
                                FROM employees_employee
                                WHERE salary > 100000
                            """)

    for employee in employees:

        print(employee.name,employee.salary)

    # 44. iterator() Streams results directly from the DB cursor, yielding one at a time.
    # Avoids queryset caching. Useful for large datasets.
    print("\n44. iterator()")

    count = 0

    for employee in Employee.objects.iterator():

        print(employee.name)

        count += 1

        if count >= 5:
            break

    # 45. union() Combines two or more querysets (same model) with set operations:
    print("\n45. union()") 

    high_salary = Employee.objects.filter(salary__gt=100000)

    female = Employee.objects.filter(gender="female")

    employees = high_salary.union(female)

    for employee in employees[:5]:

        print(employee.name)

    # 46. intersection()
    print("\n46. intersection()")

    employees = high_salary.intersection(female)

    for employee in employees:

        print(employee.name,employee.salary)

    # 47. difference()
    print("\n47. difference()")

    employees = high_salary.difference(female)

    for employee in employees:

        print(employee.name,employee.salary)

    # 48. db_manager() Allows you to run queries against a non‑default database alias
    # Execute query using specific database.
    print("\n48. db_manager()")

    total = (Employee.objects.db_manager("default").count())

    print(f"Employee Count: {total}")

    # 49. bulk_update()
    # What it does:
    # Updates many model instances in a single query. It’s more efficient than updating objects one by one.

    # When to use:
    # When you need to change the same field (or fields) on several objects at once, minimizing database round‐trips.
    # Update multiple records in one query.
    print("\n49. bulk_update()")

    employees = list(Employee.objects.all()[:10])

    for employee in employees:

        employee.salary += 1000

    Employee.objects.bulk_update(employees,["salary"])

    print(f"Updated {len(employees)} employees")

    # 50. explain()
    # What it does:
    # Returns the database’s execution plan for a queryset. This is useful for performance debugging and optimization.

    # When to use:
    # When you want to see how the database executes your query, which is helpful in tuning slow queries
    # Show database execution plan.
    print("\n50. explain()")

    plan = (Employee.objects.filter(salary__gt=100000).explain())
    print(plan)