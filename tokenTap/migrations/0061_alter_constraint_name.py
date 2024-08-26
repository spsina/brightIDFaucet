# Generated by Django 4.0.4 on 2024-08-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenTap', '0060_alter_constraint_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constraint',
            name='name',
            field=models.CharField(choices=[('core.BrightIDMeetVerification', 'BrightIDMeetVerification'), ('core.BrightIDAuraVerification', 'BrightIDAuraVerification'), ('core.HasNFTVerification', 'HasNFTVerification'), ('core.HasTokenVerification', 'HasTokenVerification'), ('core.HasTokenTransferVerification', 'HasTokenTransferVerification'), ('core.AllowListVerification', 'AllowListVerification'), ('core.HasENSVerification', 'HasENSVerification'), ('core.HasLensProfile', 'HasLensProfile'), ('core.IsFollowingLensUser', 'IsFollowingLensUser'), ('core.BeFollowedByLensUser', 'BeFollowedByLensUser'), ('core.DidMirrorOnLensPublication', 'DidMirrorOnLensPublication'), ('core.DidCollectLensPublication', 'DidCollectLensPublication'), ('core.HasMinimumLensPost', 'HasMinimumLensPost'), ('core.HasMinimumLensFollower', 'HasMinimumLensFollower'), ('core.BeFollowedByFarcasterUser', 'BeFollowedByFarcasterUser'), ('core.HasMinimumFarcasterFollower', 'HasMinimumFarcasterFollower'), ('core.DidLikedFarcasterCast', 'DidLikedFarcasterCast'), ('core.DidRecastFarcasterCast', 'DidRecastFarcasterCast'), ('core.IsFollowingFarcasterUser', 'IsFollowingFarcasterUser'), ('core.HasFarcasterProfile', 'HasFarcasterProfile'), ('core.BeAttestedBy', 'BeAttestedBy'), ('core.Attest', 'Attest'), ('core.HasDonatedOnGitcoin', 'HasDonatedOnGitcoin'), ('core.HasMinimumHumanityScore', 'HasMinimumHumanityScore'), ('core.HasGitcoinPassportProfile', 'HasGitcoinPassportProfile'), ('core.IsFollowingFarcasterChannel', 'IsFollowingFarcasterChannel'), ('core.BridgeEthToArb', 'BridgeEthToArb'), ('core.IsFollowinTwitterUser', 'IsFollowinTwitterUser'), ('core.BeFollowedByTwitterUser', 'BeFollowedByTwitterUser'), ('core.DidRetweetTweet', 'DidRetweetTweet'), ('core.DidQuoteTweet', 'DidQuoteTweet'), ('core.HasMuonNode', 'HasMuonNode'), ('core.DelegateArb', 'DelegateArb'), ('core.DelegateOP', 'DelegateOP'), ('core.DidDelegateArbToAddress', 'DidDelegateArbToAddress'), ('core.DidDelegateOPToAddress', 'DidDelegateOPToAddress'), ('core.GLMStakingVerification', 'GLMStakingVerification'), ('core.IsFollowingTwitterBatch', 'IsFollowingTwitterBatch'), ('core.IsFollowingFarcasterBatch', 'IsFollowingFarcasterBatch'), ('tokenTap.OncePerMonthVerification', 'OncePerMonthVerification'), ('tokenTap.OnceInALifeTimeVerification', 'OnceInALifeTimeVerification'), ('faucet.OptimismHasClaimedGasConstraint', 'OptimismHasClaimedGasConstraint')], max_length=255, unique=True),
        ),
    ]
