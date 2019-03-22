import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','electro.settings')

"""
PRODUCT:
[ ] Name
[ ] Price Old
[ ] Price New
"""

import django
# Import settings
django.setup()

import random
from electro_app.models import (Product, Description, Extra_Info, Review, Comments, Images)
from faker import Faker

fakegen = Faker()


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        fake_name = fakegen.name_male()

        product = Product.objects.get_or_create(name=fake_name,price_new=100,price_old=200)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
