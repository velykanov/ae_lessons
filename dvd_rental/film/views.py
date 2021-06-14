import datetime
import json
import re

from django.db.models import F
from django.http import HttpRequest, HttpResponse
from django.views import View

from .models import Film

#
# def test_index(request: HttpRequest):
#     if request.method == 'GET':
#         return HttpResponse('index')
#
#     return HttpResponse('method not allowed', status=405)


class DateJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d')

        if isinstance(o, Film):
            return {
                'title': o.title,
                'description': o.description,
                'release_date': o.release_date,
            }

        return json.JSONEncoder.default(json.JSONEncoder, o)


class DateJSONDecoder(json.JSONDecoder):
    def decode(self, s: str, _w=None):
        o = super().decode(s)
        if '__type__' in o:
            if o['__type__'] == 'Student':
                o.pop('__type__')
                return Student(**o)

        return o


class FilmView(View):
    def get(self, request: HttpRequest):
        films = Film.objects.all()  # select * from film_films
        films = Film.objects.filter(
            # title='Inception',
            release_date__lte='2020-12-31',
        )  # select * from film_films where release_date <= '2020-12-31'
        films = Film.objects.all().values(
            'title',
            'description',
            'release_date',
            # lang=F('language__name'),
        )  # select film_films.title, .., film_language.name as lang from film_films inner join film_language on
            # film_language.id = film_films.language_id

        Film.objects.all().values_list('id', 'title')
        # QuerySet([(1, 'Inception'), (2, 'Terminator'), (3, 'Back to the future')])
        Film.objects.all().values_list('id', flat=True)
        # QuerySet([1, 2, 3])

        films = list(films)

        film = Film.objects.all().first()
        # for film in films:
        #     film['release_date'] = film['release_date'].strftime('%Y-%m-%d')

        return HttpResponse(
            json.dumps({
                'film': film,
            }, cls=DateJSONEncoder),
            content_type='application/json',
        )  # JSON.stringify

    def post(self, request: HttpRequest):
        return HttpResponse('post view-index')
