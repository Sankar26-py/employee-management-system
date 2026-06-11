from django.core.management.base import (BaseCommand)
from employees.orm_examples.basic_queries import run as basic_run
from employees.orm_examples.write_queries import run as write_run
from employees.orm_examples.optimization_queries import run as optimization_run
from employees.orm_examples.postgres_queries import run as postgres_run
from employees.orm_examples.advanced_queries import run as advanced_run
from employees.orm_examples.queryset_helpers import run as query_run
from employees.orm_examples.bulk_operations import run as bulk_operations_run
from employees.orm_examples.date_queries import run as date_query_run
from employees.orm_examples.window_functions import run as window_run
from employees.orm_examples.interview_queries import run as interview_run

class Command(BaseCommand):

    help = ("Run all ORM examples")

    def handle(self,*args,**kwargs):

        self.stdout.write(self.style.SUCCESS("\nStarting ORM Demonstration\n"))

        basic_run()
        write_run()
        optimization_run()
        postgres_run()
        advanced_run() 
        query_run()
        bulk_operations_run() 
        date_query_run()
        window_run()
        interview_run()

        self.stdout.write(self.style.SUCCESS("\nORM Demonstration Complete\n"))