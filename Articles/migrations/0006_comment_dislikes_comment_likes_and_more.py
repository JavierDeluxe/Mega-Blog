# Generated by Django 4.0.3 on 2022-04-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0005_remove_article_hearts_remove_hearts_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment_second_level',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment_second_level',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
