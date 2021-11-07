from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from pretalx.common.mixins.views import PermissionRequired
from pretalx.submission.models import Submission

from .forms import YouTubeUrlForm


class YouTubeSettings(PermissionRequired, TemplateView):
    permission_required = "orga.change_settings"
    template_name = "pretalx_youtube/settings.html"

    def get_success_url(self):
        return self.request.path

    def get_object(self):
        return self.request.event

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        code = action[len("url_") :]
        try:
            submission = request.event.submissions.get(code=code)
        except Submission.DoesNotExist:
            messages.error(request, _("Could not find this talk."))
            return super().get(request, *args, **kwargs)

        form = YouTubeUrlForm(request.POST, submission=submission)
        if not form.is_valid():
            messages.error(request, form.errors)
            return super().get(request, *args, **kwargs)
        else:
            request.event.settings.set(
                f"youtube_url_{submission.code}",
                form.cleaned_data["youtube_url"],
            )
            messages.success(request, _("The URL for this talk was updated."))
            return super().get(request, *args, **kwargs)

        return super().post(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["url_forms"] = [
            YouTubeUrlForm(submission=submission)
            for submission in self.request.event.talks
        ]
        return kwargs
