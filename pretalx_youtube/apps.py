from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PluginApp(AppConfig):
    name = "pretalx_youtube"
    verbose_name = "YouTube integration"

    class PretalxPluginMeta:
        name = gettext_lazy("YouTube integration")
        author = "Toshaan Bharvani"
        description = gettext_lazy("Embed YouTube videos as session recordings")
        visible = True
        version = "0.0.1"

    def ready(self):
        from . import signals  # NOQA
