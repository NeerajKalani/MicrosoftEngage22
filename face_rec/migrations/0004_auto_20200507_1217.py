# Generated by Django 2.2 on 2020-05-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_rec', '0003_auto_20200505_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='nobody.jpg', null=True, upload_to=''),
        ),
    ]