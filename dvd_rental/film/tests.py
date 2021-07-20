from django.test import TestCase

# Create your tests here.
from .factories import FilmFactory, LanguageFactory
from .models import Film


class TestFilm(TestCase):

    def setUp(self) -> None:
        self.language = LanguageFactory()
        self.film = FilmFactory(language=self.language)
        self.client = self.client_class()

    def test_fetch(self):
        film = Film.objects.get(title=self.film.title)
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
