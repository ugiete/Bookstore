# Generated by Django 4.1.6 on 2023-02-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['id'], name='book_id_index'),
        ),
    ]