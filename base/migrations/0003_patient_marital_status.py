# Generated by Django 3.2.16 on 2022-11-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20221102_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Separated', 'Separated')], max_length=30, null=True),
        ),
    ]