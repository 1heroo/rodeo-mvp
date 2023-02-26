from django.contrib import admin
from .models import Tournament, Champion, Participant, Gallery

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Participant)
admin.site.register(Tournament)
admin.site.register(Champion)
