from django.db import models

#------------------------------------------------------------

STR_SHORT   =  10         # length of short strings
STR_MED     =  40         # length of medium strings
STR_LONG    = 100         # length of long strings
STR_REG_KEY =  20         # length of Eventbrite registration key

#------------------------------------------------------------

class Site(models.Model):
    '''Represent a site where workshops are hosted.'''

    domain     = models.CharField(max_length=STR_LONG, unique=True)
    fullname   = models.CharField(max_length=STR_LONG, unique=True)
    country    = models.CharField(max_length=STR_LONG, null=True)

    def __str__(self):
        return self.domain

#------------------------------------------------------------

class Airport(models.Model):
    '''Represent an airport (used to locate instructors).'''

    iata      = models.CharField(max_length=STR_SHORT, unique=True)
    fullname  = models.CharField(max_length=STR_LONG, unique=True)
    country   = models.CharField(max_length=STR_LONG)
    latitude  = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.iata

#------------------------------------------------------------

class Person(models.Model):
    '''Represent a single person.'''

    personal   = models.CharField(max_length=STR_LONG)
    middle     = models.CharField(max_length=STR_LONG, null=True)
    family     = models.CharField(max_length=STR_LONG)
    email      = models.CharField(max_length=STR_LONG, unique=True, null=True)
    gender     = models.CharField(max_length=STR_SHORT, null=True)
    active     = models.NullBooleanField()
    airport    = models.ForeignKey(Airport, null=True)
    github     = models.CharField(max_length=STR_MED, unique=True, null=True)
    twitter    = models.CharField(max_length=STR_MED, unique=True, null=True)
    url        = models.CharField(max_length=STR_LONG, null=True)

    def __str__(self):
        middle = ''
        if self.middle is not None:
            middle = ' {0}'.format(self.middle)
        return '{0}{1} {2} <{3}>'.format(self.personal, middle, self.family, self.email)

#------------------------------------------------------------

class Event(models.Model):
    '''Represent a single event.'''

    site       = models.ForeignKey(Site)
    start      = models.DateField()
    end        = models.DateField(null=True)
    slug       = models.CharField(max_length=STR_LONG, unique=True)
    kind       = models.CharField(max_length=STR_SHORT)
    reg_key    = models.CharField(max_length=STR_REG_KEY, null=True)
    attendance = models.IntegerField(null=True)

    def __str__(self):
        return self.slug

#------------------------------------------------------------

class Role(models.Model):
    '''Enumerate roles in workshops.'''

    role       = models.CharField(max_length=STR_MED)

    def __str__(self):
        return self.role

#------------------------------------------------------------

class Task(models.Model):
    '''Represent who did what at events.'''

    event      = models.ForeignKey(Event)
    person     = models.ForeignKey(Person)
    role       = models.ForeignKey(Role)

    def __str__(self):
        return '{0}/{1}={2}'.format(self.event, self.person, self.task)