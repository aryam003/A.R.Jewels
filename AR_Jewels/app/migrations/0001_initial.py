# Generated by Django 5.1.2 on 2024-11-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jewels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewels_id', models.TextField()),
                ('category', models.TextField()),
                ('jewels_name', models.TextField()),
                ('price', models.IntegerField()),
                ('offer_price', models.IntegerField()),
                ('description', models.TextField()),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]
