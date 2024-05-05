from django.utils.translation import ugettext_lazy as _
from weblate.addons.events import EVENT_PRE_COMMIT
from weblate.addons.scripts import BaseScriptAddon


class CheckerAddon(BaseScriptAddon):
    """Pre commit script example addon."""
