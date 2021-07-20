from dataclasses import dataclass
import factory

from .models import Film, Language


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language

    name = factory.Faker('pystr')


class FilmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Film

    title = factory.Faker('pystr')
    description = factory.Faker('pystr')
    release_date = factory.Faker('date_object')
    language = factory.SubFactory(LanguageFactory)
