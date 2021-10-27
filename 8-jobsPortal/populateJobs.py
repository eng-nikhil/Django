#### To be Called Manually using "python populate.py delhi 20" when want to popluate 20 delhi jobs

import os
#Required to work with projects Model Class
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsPortal.settings')
import django
django.setup()
#####################
import sys # for command line argv parameters

from jobsPortalApp.models import *
from faker import Faker
from random import *

fake = Faker()

def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
    
def populate(location,n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','TeamLead','Software Engineer'))
        feligibility=fake.random_element(elements=('M.Tech','B.Tech','Phd','MCA'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        if location=='bangalore':
            bangalorejobs_records=bangalorejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
        elif location=='delhi':
            delhijobs_records=delhijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
        else:
            punejobs_records=punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

populate(sys.argv[1],int(sys.argv[2]))
        

