# Generated by Django 3.2.16 on 2022-11-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(choices=[('O', 'O'), ('A', 'A'), ('B', 'B'), ('AB', 'AB')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('W', 'W'), ('NON_BINARY', 'NON_BINARY')], max_length=30, null=True),
        ),
    ]