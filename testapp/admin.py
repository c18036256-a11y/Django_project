from django.contrib import admin

# Register your models here.
from testapp.models import Movie
class MovieAdmin(admin.ModelAdmin):
    mov_list=['rating','mname','hero','heroine']
admin.site.register(Movie,MovieAdmin)