# Generated by Django 4.0.3 on 2022-04-01 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0006_rename_hearts_article_hearts_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hearts',
            name='amount',
        ),
    ]