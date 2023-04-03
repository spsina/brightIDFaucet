# Generated by Django 4.0.4 on 2023-04-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_alter_wallet_wallet_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_type',
            field=models.CharField(choices=[('EVM', 'EVM'), ('Solana', 'Solana'), ('Lightning', 'Lightning'), ('NONEVM', 'Non-EVM')], max_length=10),
        ),
    ]