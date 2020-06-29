import uuid
import roman

from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import (
    PersonManager, MoviManager,
    DirectorManager, ProducerManager, CastManager)

# Create your models here.

class Alias(models.Model):
    person = models.ForeignKey(
        'Person', on_delete=models.CASCADE,
        related_name='aliasses')
    name = models.CharField(
        _("alias name"), max_length=50)
    
    class Meta:
        unique_together = ('person', 'name')
    
    def __str__(self):
        return self.name

class Person(models.Model):
    FEMALE = 1
    MALE = 2
    SEX = (
        (FEMALE, _("FEMALE")),
        (MALE, _("MALE"))
    )
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    first_name = models.CharField(
        _("first name"), max_length=50)
    last_name = models.CharField(
        _("last name"), max_length=50)
    sex = models.SmallIntegerField(
        _("sex"), choices=SEX)

    @property
    def fullname(self):
        return "%s %s"%(self.first_name, self.last_name)

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")
    
    objects = PersonManager()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Movie(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    title = models.CharField(
        _("title"), max_length=100)
    release_year = models.PositiveIntegerField(_("release year"))

    directors = models.ManyToManyField(
        to=Person,
        through='Director',
        related_name='movies_as_director',
    )

    producers = models.ManyToManyField(
        to=Person,
        through='Producer',
        related_name='movies_as_producer'
    )

    casting = models.ManyToManyField(
        to=Person,
        through='Cast',
        related_name='movies_as_casting'
    )

    @property
    def roman_release_year(self):
        return roman.toRoman(self.release_year)

    objects = MoviManager()

    class Meta:
        verbose_name = _("movie")
        verbose_name_plural = _("movies")
        unique_together = ('title', 'release_year')
        
    
    def __str__(self):
        return "%s (%s)"%(
            self.title, self.roman_release_year)

class Director(models.Model):

    person = models.ForeignKey(
        Person, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(
        Movie, on_delete=models.DO_NOTHING)

    objects = DirectorManager()

    class Meta:
        verbose_name = _("director")
        verbose_name_plural = _("directors")
        unique_together = ('person', 'movie')
    
    def __str__(self):
        return "%s %s" % (
            self.person, self.movie)

class Producer(models.Model):

    person = models.ForeignKey(
        Person, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(
        Movie, on_delete=models.DO_NOTHING)

    objects = ProducerManager()

    class Meta:
        verbose_name = _("producer")
        verbose_name_plural = _("producers")
        unique_together = ('person', 'movie')
    
    def __str__(self):
        return "%s %s" % (
            self.person, self.movie)

class Cast(models.Model):

    person = models.ForeignKey(
        Person, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(
        Movie, on_delete=models.DO_NOTHING)

    objects = CastManager()

    class Meta:
        verbose_name = _("cast")
        verbose_name_plural = _("casts")
        unique_together = ('person', 'movie')
    
    def __str__(self):
        return "%s %s" % (
            self.person, self.movie)
