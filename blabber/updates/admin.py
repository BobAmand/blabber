from django.contrib import admin
from .models import Status, Favorite


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'test', 'posted_at','favorite_set']

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']


admin.site.register(Status, StatusAdmin)
admin.site.register(Favorite)
