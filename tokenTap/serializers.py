from faucet.serializers import SmallChainSerializer
from rest_framework import serializers
from permissions.serializers import PermissionSerializer
from tokenTap.models import TokenDistribution, TokenDistributionClaim


class DetailResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        pass


class TokenDistributionSerializer(serializers.ModelSerializer):
    chain = SmallChainSerializer()
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = TokenDistribution
        fields = [
            "id",
            "name",
            "distributor",
            "distributor_url",
            "discord_url",
            "twitter_url",
            "image_url",
            "token",
            "token_address",
            "amount",
            "chain",
            "permissions",
            "created_at",
            "deadline",
            "max_number_of_claims",
            "number_of_claims",
            "notes",
            "is_expired",
            "is_maxed_out",
            "is_claimable",
        ]


class SmallTokenDistributionSerializer(serializers.ModelSerializer):
    chain = SmallChainSerializer()
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = TokenDistribution
        fields = [
            "id",
            "name",
            "distributor",
            "distributor_url",
            "discord_url",
            "twitter_url",
            "image_url",
            "token",
            "token_address",
            "amount",
            "chain",
            "permissions",
            "created_at",
            "deadline",
            "max_number_of_claims",
            "notes",
        ]


class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenDistributionClaim
        fields = ["user", "token", "amount", "nonce", "signature"]


class TokenDistributionClaimSerializer(serializers.ModelSerializer):
    token_distribution = SmallTokenDistributionSerializer()
    payload = serializers.SerializerMethodField()

    class Meta:
        model = TokenDistributionClaim
        fields = [
            "id",
            "token_distribution",
            "user_profile",
            "created_at",
            "payload",
            "status",
            "tx_hash",
        ]

    def get_payload(self, obj):
        return PayloadSerializer(obj).data


class TokenDistributionClaimResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()
    signature = TokenDistributionClaimSerializer()