# Generated by Django 4.0.3 on 2022-04-03 15:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0004_alter_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hearts',
        ),
        migrations.RemoveField(
            model_name='hearts',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='hearts',
            name='comment',
        ),
        migrations.AddField(
            model_name='article',
            name='hearts_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment_second_level',
            name='article_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Articles.article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment_second_level',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hearts',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Articles.article'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
