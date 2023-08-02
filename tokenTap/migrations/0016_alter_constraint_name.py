# Generated by Django 4.0.4 on 2023-07-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenTap', '0015_constraint_alter_tokendistribution_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constraint',
            name='name',
            field=models.CharField(choices=[('BrightIDMeetVerification', 'BrightIDMeetVerification'), ('BrightIDAuraVerification', 'BrightIDAuraVerification'), ('OncePerWeekVerification', 'OncePerWeekVerification'), ('OncePerMonthVerification', 'OncePerMonthVerification'), ('OnceInALifeTimeVerification', 'OnceInALifeTimeVerification')], max_length=255, unique=True),
        ),
    ]