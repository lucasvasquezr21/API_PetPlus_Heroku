# Generated by Django 4.1.1 on 2022-10-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
    ]
