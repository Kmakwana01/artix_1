# Generated by Django 4.2.7 on 2023-11-25 06:36

import autoslug.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lifestylemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img_src', models.CharField(max_length=200)),
                ('categori', models.CharField(max_length=200)),
                ('main_heading', models.CharField(max_length=200)),
                ('description', tinymce.models.HTMLField()),
                ('img_src_two', models.CharField(max_length=200)),
                ('description_two', tinymce.models.HTMLField()),
                ('img_src_three', models.CharField(max_length=200)),
                ('description_three', tinymce.models.HTMLField()),
                ('img_src_four', models.CharField(max_length=200)),
                ('img_src_five', models.CharField(max_length=200)),
                ('description_four', tinymce.models.HTMLField()),
                ('img_src_six', models.CharField(max_length=200)),
                ('new_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='main_heading', unique=True)),
            ],
        ),
    ]
