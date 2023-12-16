from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

from authentication.helpers import BRIGHTID_SOULDBOUND_INTERFACE
from core.models import NetworkTypes


class ProfileManager(models.Manager):
    def get_or_create(self, first_context_id):
        try:
            return super().get_queryset().get(initial_context_id=first_context_id)
        except UserProfile.DoesNotExist:
            _user = User.objects.create_user(username=first_context_id)
            _profile = UserProfile(user=_user, initial_context_id=first_context_id)
            _profile.save()
            return _profile


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="profile")
    initial_context_id = models.CharField(max_length=512, unique=True)

    username = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=r"^[\w.@+-]+$",
                message="Username can only contain letters, digits and @/./+/-/_.",
            ),
        ],
        null=True,
        blank=True,
        unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    objects = ProfileManager()

    @property
    def age(self):
        if self.created_at is None:
            return -1
        return timezone.now() - self.created_at

    @property
    def is_meet_verified(self):
        (
            is_verified,
            context_ids,
        ) = BRIGHTID_SOULDBOUND_INTERFACE.get_verification_status(
            self.initial_context_id, "Meet"
        )

        return is_verified

    @property
    def is_aura_verified(self):
        (
            is_verified,
            context_ids,
        ) = BRIGHTID_SOULDBOUND_INTERFACE.get_verification_status(
            self.initial_context_id, "Aura"
        )

        return is_verified

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.username:
            self.username = f"User{self.pk}"
            super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username if self.username else f"User{self.pk}"

    @staticmethod
    def user_count():
        cached_user_count = cache.get("user_profile_count")
        if cached_user_count:
            return cached_user_count
        count = UserProfile.objects.count()
        cache.set("user_profile_count", count, 300)
        return count


class Wallet(models.Model):
    wallet_type = models.CharField(choices=NetworkTypes.networks, max_length=10)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.PROTECT, related_name="wallets"
    )
    address = models.CharField(max_length=512, unique=True)

    class Meta:
        unique_together = (("wallet_type", "user_profile"),)

    def __str__(self):
        return (
            f"{self.wallet_type} Wallet for profile with contextId "
            f"{self.user_profile.initial_context_id}"
        )
