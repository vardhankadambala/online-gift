# Generated by Django 3.2.4 on 2021-09-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life_app', '0003_cart1'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart1',
            name='u_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
