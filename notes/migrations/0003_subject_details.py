# Generated by Django 5.1 on 2025-07-09 11:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
