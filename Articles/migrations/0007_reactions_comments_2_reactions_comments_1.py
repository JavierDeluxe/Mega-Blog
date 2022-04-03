# Generated by Django 4.0.3 on 2022-04-03 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0006_comment_dislikes_comment_likes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='reactions_comments_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
                ('dislike', models.BooleanField()),
                ('coment_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.comment_second_level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='reactions_comments_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
                ('dislike', models.BooleanField()),
                ('coment_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]