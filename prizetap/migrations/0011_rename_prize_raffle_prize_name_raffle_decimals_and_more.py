# Generated by Django 4.0.4 on 2023-07-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prizetap', '0010_raffleentry_claiming_prize_tx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raffle',
            old_name='prize',
            new_name='prize_name',
        ),
        migrations.AddField(
            model_name='raffle',
            name='decimals',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='raffle',
            name='nft_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='raffle',
            name='prize_amount',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raffle',
            name='prize_asset',
            field=models.CharField(default='0x0', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raffle',
            name='prize_symbol',
            field=models.CharField(default='ETH', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raffle',
            name='token_uri',
            field=models.TextField(blank=True, null=True),
        ),
    ]
