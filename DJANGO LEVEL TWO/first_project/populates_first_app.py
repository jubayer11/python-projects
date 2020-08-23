import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django

django.setup()

# Fake POP Script

import random
from first_app.models import AccessRecord, Webpage, Topic,User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketing Place', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new Webpage

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


def populate1(N=10):
    for entry in range(N):
        first_name = fakegen.name()
        last_name = fakegen.name()
        email=fakegen.email()
        x=User.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)[0]


if __name__ == '__main__':
    print("populating Script!")
    #populate(20)
    populate1(20)
    print("populating Done")
