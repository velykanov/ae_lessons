import datetime

from django.contrib import admin, messages

# Register your models here.
from .models import Film


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # ('__str__',)

    def save_model(self, request, obj: Film, form, change):
        if change:
            old_film = Film.objects.get(id=obj.id)  # Film(id) or Exception
            # old_film = Film.objects.filter(id=obj.id).first()  # Film(id) or None
            if old_film.release_date.year < obj.release_date.year:
                messages.error(request, 'The year was modified')
                return
        # if obj.release_date > datetime.datetime.now().date():
        #     # obj.description = f'Film is in the future: {obj.description}'
        #     messages.error(request, 'Films in the future are not allowed')
        #     return

        return super().save_model(request, obj, form, change)


admin.site.register(Film, FilmAdmin)
