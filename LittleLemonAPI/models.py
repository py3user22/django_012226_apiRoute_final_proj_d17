from django.db.models import (
    Model, CharField, DecimalField, SmallIntegerField,
    SlugField, ForeignKey, CASCADE, PROTECT, TextField, DateField, IntegerField,
)
import datetime


# Create your models here.
# video Filtering & searching   --@010626

class Category( Model ):
    slug = SlugField()
    title = CharField( max_length=250 )

    def __str__(self):
        return self.title


# video = Resturant menu API with DRF  --@010226'

class MenuItem( Model ):
    title = CharField( max_length=255 )
    price = DecimalField( max_digits=6, decimal_places=2 )
    inventory = SmallIntegerField()
    category = ForeignKey( Category, on_delete=PROTECT, default=1 )

    def __str__(self):
        return self.title


# _________________________________
# _____

# 011126' create a new model for delivery orders

class Delivery( Model ):
    """ 111 new model for delivery """
    # Date picker (Django admin + forms automatically show a calendar widget)
    delivery_date = DateField(default=datetime.date.today)

    # Time slot choices: 9am, 12pm, 3pm, 6pm, 9pm
    DELIVERY_CREW_GROUP_CHOICES = [ ('none', 'None'), ('dc1', 'DC1'), ('dc2', 'DC2'), ('dc3', 'DC3') ]
    DELIVERY_STATUS_CHOICES = [ ('yes', 'Yes'), ('no', 'No'), ('progress', 'In Progress'), ]
    TIME_SLOT_CHOICES = [
        ('09:00', '9:00 AM'), ('12:00', '12:00 PM'),
        ('15:00', '3:00 PM'), ('18:00', '6:00 PM'), ('21:00', '9:00 PM'),
    ]

    time_slot = CharField( max_length=5, choices=TIME_SLOT_CHOICES, default='12:00' )

    delivery_status = CharField( max_length=10, choices=DELIVERY_STATUS_CHOICES, default='progress' )
    name = CharField(max_length=100)
    address = TextField(blank=True, null=True)
    notes = TextField(blank=True, null=True)
    delivery_assigned_to = CharField( max_length=4, choices=DELIVERY_CREW_GROUP_CHOICES, default='none' )

    def __str__(self):
        return f"{self.delivery_date} @ {self.time_slot}"


# _________________________________
# _________________________________