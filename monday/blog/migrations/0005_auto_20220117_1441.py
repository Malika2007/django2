# Generated by Django 3.1.1 on 2022-01-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='image.jpeg', upload_to=''),
        ),
    ]
