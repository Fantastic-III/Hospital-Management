# Generated by Django 5.0.7 on 2025-01-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0003_alter_appointment_time_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(max_length=50),
        ),
    ]
