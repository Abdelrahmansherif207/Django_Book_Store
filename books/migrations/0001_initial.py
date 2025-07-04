# Generated by Django 5.2.3 on 2025-07-04 14:57

import books.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[books.models.validate_category_name])),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[books.models.validate_title_length])),
                ('desc', models.TextField()),
                ('rate', models.DecimalField(decimal_places=1, max_digits=3)),
                ('views', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='books.category')),
            ],
        ),
        migrations.CreateModel(
            name='ISBN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_title', models.CharField(max_length=100)),
                ('book_title', models.CharField(max_length=100)),
                ('isbn_number', models.CharField(editable=False, max_length=13, unique=True)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]
