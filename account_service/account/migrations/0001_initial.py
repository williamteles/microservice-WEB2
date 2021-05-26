# Generated by Django 3.2.3 on 2021-05-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=10, unique=True)),
                ('balance', models.DecimalField(decimal_places=10, max_digits=18)),
                ('owner_id', models.IntegerField(unique=True)),
            ],
        ),
    ]
