# Generated by Django 2.2.5 on 2019-10-22 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='chats', to='chat.Contact'),
        ),
    ]