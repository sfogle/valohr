from django.db import models

#class Poll(models.Model):
#    question = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')

#class Choice(models.Model):
#    poll = models.ForeignKey(Poll)
#    choice = models.CharField(max_length=200)
#    votes = models.IntegerField()

class Room(models.Model):
    room_name = models.CharField('name', max_length=25)
    #beds = models.ManyToManyField(Bed)
    price_per_night = models.DecimalField('price per night', max_digits=6, decimal_places=2)
    price_per_week = models.DecimalField('price per week', max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.room_name


class Bed(models.Model):
    TWIN_SIZE = 1
    DOUBLE_SIZE = 2
    QUEEN_SIZE = 3
    KING_SIZE = 4
    SIZES = (
        (TWIN_SIZE, 'Twin'),
        (DOUBLE_SIZE, 'Double'),
        (QUEEN_SIZE, 'Queen'),
        (KING_SIZE, 'King'),
    )
    size = models.IntegerField(choices=SIZES)
    room = models.ForeignKey(Room)

    def __unicode__(self):
        return self.get_size_display()

class Reservation(models.Model):
    room = models.ForeignKey(Room)
    arrival_date = models.DateField()
    departure_date = models.DateField()

