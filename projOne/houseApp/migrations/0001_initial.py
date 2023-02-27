# Generated by Django 4.1.7 on 2023-02-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='houseListingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('price', models.IntegerField()),
                ('squareField', models.IntegerField()),
                ('noBedrooms', models.IntegerField()),
                ('address', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]