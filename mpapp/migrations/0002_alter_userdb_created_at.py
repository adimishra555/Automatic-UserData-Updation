# Generated by Django 5.0.3 on 2024-03-21 05:00

from django.db import migrations, models
class Migration(migrations.Migration):

    dependencies = [
        ('mpapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdb',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
