#### To be Called Manually using "python populate.py delhi 20" when want to popluate 20 delhi jobs

import os
#Required to work with projects Model Class
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudfbvProject.settings')
import django
django.setup()
#####################
import sys # for command line argv parameters

from crudfbvApp.models import *
from faker import Faker
from random import *

fake = Faker()
   
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=fake.name()
        fsal=randint(10001,99999)
        faddress=fake.city()
        Employee_records=Employee.objects.get_or_create(enum=feno,ename=fename,esal=fsal,eaddr=faddress)

populate(int(sys.argv[1]))
        

 