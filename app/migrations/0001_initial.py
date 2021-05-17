# Generated by Django 3.1.3 on 2021-05-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('pno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
