# Generated by Django 5.2 on 2025-05-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1 - Very Bad'), (2, '2 - Bad'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
