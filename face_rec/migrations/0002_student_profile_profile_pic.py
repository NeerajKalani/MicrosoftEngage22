# Generated by Django 2.2 on 2020-05-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_rec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/nobody.jpg', null=True, upload_to=''),
        ),
    ]
