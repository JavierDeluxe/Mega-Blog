# Generated by Django 4.0.3 on 2022-04-03 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0008_rename_coment_1_reactions_comments_1_coment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reactions_comments_1',
            old_name='coment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='reactions_comments_2',
            old_name='coment',
            new_name='comment',
        ),
    ]
