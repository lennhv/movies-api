from django.db import models
from django.db import transaction


def get_instance(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist as e:
        return None

class PersonManager(models.Manager):

    def add(self, first_name=None, last_name=None,sex=None, aliasses=[] ):
        from .models import Alias
        with transaction.atomic():
            instance=self.model(
                first_name=first_name,
                last_name=last_name,
                sex=sex)
            instance.save()
            for alias in aliasses:
                Alias(name=alias["name"], person=instance).save()
        return instance

    def update_instance(self, instance, data):
        from .models import Alias
        aliasses = data.get("aliasses", [])
        if "aliasses" in data:
            del data["aliasses"]
        with transaction.atomic():
            for attr, value in data.items():
                setattr(instance, attr, value)
            if aliasses:
                Alias.objects.filter(person=instance).delete()
                for alias in aliasses:
                    Alias(name=alias["name"], person=instance).save()
            instance.save(update_fields=data.keys())
        return instance

    def add_alias(self, instance, data):
        from .models import Alias
        with transaction.atomic():
            for alias in data['aliasses']:
                Alias(name=alias["name"], person=instance).save()
        return instance

    def del_alias(self, instance, data):
        from .models import Alias
        Alias.objects.filter(person=instance, name=data["name"]).delete()
        return instance

    def add_movie_as_director(self, instance, data):
        from .models import Movie
        with transaction.atomic():
            for movie in data["movies"]:
                mv = get_instance(Movie, title=movie["title"], release_year=movie["release_year"])
                if mv:
                    instance.movies_as_director.add(mv)
        return instance

    def del_directed_movie(self, instance, data):
        from .models import Movie
        person = get_instance(Movie, id=data.get("movie_id"))
        if person:
            instance.movies_as_director.remove(person)
        return instance

    def add_movie_as_producer(self, instance, data):
        from .models import Movie
        with transaction.atomic():
            for movie in data["movies"]:
                mv = get_instance(Movie, title=movie["title"], release_year=movie["release_year"])
                if mv:
                    instance.movies_as_producer.add(mv)
        return instance

    def del_producted_movie(self, instance, data):
        from .models import Movie
        person = get_instance(Movie, id=data.get("movie_id"))
        if person:
            instance.movies_as_producer.remove(person)
        return instance

    def add_movie_as_casting(self, instance, data):
        from .models import Movie
        with transaction.atomic():
            for movie in data["movies"]:
                mv = get_instance(Movie, title=movie["title"], release_year=movie["release_year"])
                if mv:
                    instance.movies_as_casting.add(mv)
        return instance

    def del_casted_movie(self, instance, data):
        from .models import Movie
        person = get_instance(Movie, id=data.get("movie_id"))
        if person:
            instance.movies_as_casting.remove(person)
        return instance


class MoviManager(models.Manager):

    def add(self, title=None, release_year=None ):
        from .models import Alias
        with transaction.atomic():
            instance=self.model(
                title=title,
                release_year=release_year)
            instance.save()
        return instance

    def update_instance(self, instance, data):
        from .models import Alias
        with transaction.atomic():
            for attr, value in data.items():
                setattr(instance, attr, value)
            instance.save(update_fields=data.keys())
        return instance

    def add_director(self, instance, data):
        from .models import Person
        with transaction.atomic():
            for p in data["directors"]:
                person = get_instance(Person, id=p.get("id"))
                if not person:
                    continue
                instance.directors.add(person)
        return instance

    def del_director(self, instance, data):
        from .models import Person
        person = get_instance(Person, id=data.get("person_id"))
        if person:
            instance.directors.remove(person)
        return instance

    def add_producer(self, instance, data):
        from .models import Person
        with transaction.atomic():
            for p in data["producers"]:
                person = get_instance(Person, id=p.get("id"))
                if not person:
                    continue
                instance.producers.add(person)
        return instance

    def del_producer(self, instance, data):
        from .models import Person
        person = get_instance(Person, id=data.get("person_id"))
        if person:
            instance.producers.remove(person)
        return instance

    def add_casting(self, instance, data):
        from .models import Person
        with transaction.atomic():
            for p in data["casting"]:
                person = get_instance(Person, id=p.get("id"))
                if not person:
                    continue
                instance.casting.add(person)
        return instance

    def del_producer(self, instance, data):
        from .models import Person
        person = get_instance(Person, id=data.get("person_id"))
        if person:
            instance.casting.remove(person)
        return instance


class DirectorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class ProducerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class CastManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()