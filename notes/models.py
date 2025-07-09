from django.db import models
from ckeditor.fields import RichTextField

from ckeditor.fields import RichTextField

class Subject(models.Model):
    name = models.CharField(max_length=200)
    details = RichTextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subsubjects')

    def __str__(self):
        return self.name if not self.parent else f"{self.parent} > {self.name}"

class Note(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextField()

    def __str__(self):
        return self.title
