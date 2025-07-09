from django.contrib import admin
from .models import Subject, Note

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    fields = ('name', 'details', 'parent')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Note)
