from django.db import models


class Film(models.Model):
    title = models.TextField()
    description = models.TextField()
    release_date = models.DateField()

    language = models.ForeignKey('film.Language', on_delete=models.CASCADE)
    # actors = models.ManyToManyField('actor.Actor')

    def __str__(self):
        return f'Film(title={self.title})'

    def to_dict(self):
        return {
            'film': {
                'title': self.title,
                'description': self.description,
                'release_date': self.release_date.strftime('%Y-%m-%d'),
            },
        }


class Language(models.Model):
    name = models.TextField()


class FilmActor(models.Model):
    film = models.ForeignKey('film.Film', on_delete=models.CASCADE)
    actor = models.ForeignKey('actor.Actor', on_delete=models.CASCADE)
    last_update = models.DateField()
