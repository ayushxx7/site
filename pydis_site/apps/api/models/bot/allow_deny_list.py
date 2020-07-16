from django.db import models

from pydis_site.apps.api.models.mixins import ModelReprMixin, ModelTimestampMixin


class AllowDenyList(ModelTimestampMixin, ModelReprMixin, models.Model):
    """An item that is either allowed or denied."""

    AllowDenyListType = models.TextChoices(
        'AllowDenyListType',
        'GUILD_INVITE_ID '
        'FILE_FORMAT '
        'DOMAIN_NAME '
        'WORD_WATCHLIST '
    )
    type = models.CharField(
        max_length=50,
        help_text="The type of allowlist this is on.",
        choices=AllowDenyListType.choices,
    )
    allowed = models.BooleanField(
        help_text="Whether this item is on the allowlist or the denylist."
    )
    content = models.TextField(
        help_text="The data to add to the allow or denylist."
    )

    class Meta:
        """Metaconfig for this model."""

        # This constraint ensures only one allow or denylist with the
        # same content can exist. This means that we cannot have both an allow
        # and a deny for the same item, and we cannot have duplicates of the
        # same item.
        constraints = [
            models.UniqueConstraint(fields=['content', 'type'], name='unique_allow_deny_list'),
        ]