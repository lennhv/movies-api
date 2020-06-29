from django.contrib import admin

# Register your models here.

from .models import (
    Person, Movie, Alias,
    Producer, Director, Cast )


site = admin.site

class PersonAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'sex', 'aliasses')

    def aliasses(self, obj):
        return ", ".join([alias.name for alias in obj.aliasses.all()])
        # return ''

    aliasses.short_description = 'Aliasses'

site.register(Person,PersonAdmin)

class MoviAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year')

site.register(Movie)

class AliasAdmin(admin.ModelAdmin):
    list_display = ('person', 'name', )

site.register(Alias, AliasAdmin)


class CastAdmin(admin.ModelAdmin):
    list_display = ('movie', 'person')

site.register(Cast, CastAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('movie', 'person')

site.register(Director, DirectorAdmin)

class ProducerAdmin(admin.ModelAdmin):
    list_display = ('movie', 'person')

site.register(Producer, ProducerAdmin)


