# Generated by Django 4.1.1 on 2022-10-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id_color', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'color',
                'managed': False,
            },
        ),
    ]
