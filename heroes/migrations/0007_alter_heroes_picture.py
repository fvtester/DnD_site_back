# Generated by Django 4.2.4 on 2023-10-01 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0006_alter_heroes_hero_class_alter_heroes_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroes',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
