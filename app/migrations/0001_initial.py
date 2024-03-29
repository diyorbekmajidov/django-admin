# Generated by Django 4.2.4 on 2024-03-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConcertCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'concert category',
                'verbose_name_plural': 'concert categories',
                'ordering': ['-name'],
            },
        ),
    ]
