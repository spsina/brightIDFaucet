# Generated by Django 4.0.4 on 2024-05-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prizetap', '0058_alter_constraint_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constraint',
            name='name',
            field=models.CharField(choices=[('core.BrightIDMeetVerification', 'BrightIDMeetVerification'), ('core.BrightIDAuraVerification', 'BrightIDAuraVerification'), ('core.HasNFTVerification', 'HasNFTVerification'), ('core.HasTokenVerification', 'HasTokenVerification'), ('core.HasTokenTransferVerification', 'HasTokenTransferVerification'), ('core.AllowListVerification', 'AllowListVerification'), ('core.HasENSVerification', 'HasENSVerification'), ('core.HasLensProfile', 'HasLensProfile'), ('core.IsFollowingLensUser', 'IsFollowingLensUser'), ('core.BeFollowedByLensUser', 'BeFollowedByLensUser'), ('core.DidMirrorOnLensPublication', 'DidMirrorOnLensPublication'), ('core.DidCollectLensPublication', 'DidCollectLensPublication'), ('core.HasMinimumLensPost', 'HasMinimumLensPost'), ('core.HasMinimumLensFollower', 'HasMinimumLensFollower'), ('core.BeFollowedByFarcasterUser', 'BeFollowedByFarcasterUser'), ('core.HasMinimumFarcasterFollower', 'HasMinimumFarcasterFollower'), ('core.DidLikedFarcasterCast', 'DidLikedFarcasterCast'), ('core.DidRecastFarcasterCast', 'DidRecastFarcasterCast'), ('core.IsFollowingFarcasterUser', 'IsFollowingFarcasterUser'), ('core.HasFarcasterProfile', 'HasFarcasterProfile'), ('core.BeAttestedBy', 'BeAttestedBy'), ('core.Attest', 'Attest'), ('core.HasMinimumHumanityScore', 'HasMinimumHumanityScore'), ('core.HasGitcoinPassportProfile', 'HasGitcoinPassportProfile'), ('prizetap.HaveUnitapPass', 'HaveUnitapPass'), ('prizetap.NotHaveUnitapPass', 'NotHaveUnitapPass'), ('faucet.OptimismDonationConstraint', 'OptimismDonationConstraint'), ('faucet.OptimismClaimingGasConstraint', 'OptimismClaimingGasConstraint')], max_length=255, unique=True),
        ),
    ]
