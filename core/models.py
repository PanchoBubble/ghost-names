from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# ----------------------------------------------- #
# Models:
# ----------------------------------------------- #
class GhostName(models.Model):
    """
    Simple Ghost model
    """
    name = models.TextField(_("Ghost Name"), max_length=40, unique=True)
    description = models.TextField(_("Gosht Description"), max_length=400, null=True, blank=True)

    user = models.OneToOneField(
        User, verbose_name=_("Owner"), on_delete=models.DO_NOTHING, null=True, blank=True
    )

    first_name = models.TextField(_("First Name"), max_length=40, blank=True, null=True)
    last_name = models.TextField(_("Last Name"), max_length=40, blank=True, null=True)
