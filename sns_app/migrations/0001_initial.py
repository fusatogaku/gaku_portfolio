# Generated by Django 3.2.6 on 2021-08-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('snsimage', models.ImageField(upload_to='')),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
                ('read', models.IntegerField(blank=True, default=0, null=True)),
                ('readperson', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
