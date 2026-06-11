from employees.models import Employee


# 35. reverse() 
Employee.objects.order_by("salary").reverse()

# 36. earliest()
Employee.objects.earliest("joining_date")

# 37. latest()
Employee.objects.latest("joining_date")

# 38. first()
Employee.objects.first()

# 39. last()
Employee.objects.last()

# 40. count()
Employee.objects.count()

# 41. get_or_create()
Employee.objects.get_or_create(email="sample@test.com")

# 42. update_or_create()
Employee.objects.update_or_create(
    email="sample@test.com",
    defaults={
        "salary": 90000
    }
)