# Generated by Django 4.0.3 on 2022-04-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0004_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hearts',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
