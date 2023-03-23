# Generated by Django 4.0.4 on 2023-03-12 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_temporarywalletaddress'),
        ('faucet', '0033_claimreceipt_bright_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimreceipt',
            name='user_profile',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='claims', to='authentication.userprofile'),
        ),
    ]