# Generated by Django 4.0.6 on 2022-09-13 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestamo',
            options={'managed': False, 'ordering': ['loan_id']},
        ),
    ]