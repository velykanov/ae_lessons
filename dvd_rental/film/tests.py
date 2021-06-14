import datetime

from django.test import Client, TestCase

# Create your tests here.
from .models import Film, Language


class TestFilm(TestCase):

    def setUp(self) -> None:
        self.language = Language.objects.create(name='test_en')
        self.film = Film.objects.create(
            title='Test film',
            description='Test desc',
            release_date=datetime.datetime.now().date(),
            language_id=self.language.id,
        )
        self.client = self.client_class()

    def test_fetch(self):
        film = Film.objects.get(title='Test film')
        self.assertEqual(film.title, self.film.title)  # film.title == self.film.title
        self.assertEqual(film.id, self.film.id)

    def test_api_get(self):
        response = self.client.get('/film/films/')
        data = response.json()  # dict

        self.assertTrue(response.status_code == 200)  # self.assertTrue(True)
        # self.assertEqual(
        #     {
        #         'film': {
        #             'title': self.film.title,
        #             'description': self.film.description,
        #             'release_date': self.film.release_date.strftime('%Y-%m-%d'),
        #         },
        #     },
        #     data,
        # )
        self.assertTrue('film' in data)
        self.assertEqual(
            {
                'title': self.film.title,
                'description': self.film.description,
                'release_date': self.film.release_date.strftime('%Y-%m-%d'),
            },
            data['film'],
        )

        self.assertEqual(self.film.to_dict(), data)
