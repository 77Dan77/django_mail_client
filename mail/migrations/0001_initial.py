# Generated by Django 3.2.4 on 2021-06-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=254, verbose_name='Получатель')),
                ('subject', models.CharField(max_length=200, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Текст сообщения')),
            ],
        ),
    ]
