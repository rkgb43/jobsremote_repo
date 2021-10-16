import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djProject.settings')
import django
django.setup()
from testapp.models import *
from faker import Faker
from random import *
fake=Faker()
   
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project manage', 'team lead', 'system manager'))
        feligibility=fake.random_element(elements=('b tech', 'mtech', 'bca'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        mumbaijobs_record=mumjobs.objects.get_or_create(date=fdate ,company=fcompany,title=ftitle ,eligibility=feligibility ,email=femail ,phonenumber=fphonenumber ,address=faddress)
populate(10)



