# Generated by Django 4.2.4 on 2023-08-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='img')),
                ('desc', models.TextField()),
            ],
        ),
    ]
