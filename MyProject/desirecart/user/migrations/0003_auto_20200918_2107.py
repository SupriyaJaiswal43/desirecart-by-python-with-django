# Generated by Django 3.1 on 2020-09-18 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_addtocart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtocart',
            old_name='odatde',
            new_name='odate',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='odatde',
            new_name='odate',
        ),
    ]
