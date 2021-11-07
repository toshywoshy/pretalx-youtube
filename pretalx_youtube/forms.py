from django import forms
from django.utils.translation import gettext_lazy as _


class YouTubeUrlForm(forms.Form):

    youtube_url = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        self.submission = kwargs.pop("submission")
        initial = kwargs.get("initial", dict())
        initial["youtube_url"] = self.submission.event.settings.get(
            f"youtube_url_{self.submission.code}"
        )
        kwargs["initial"] = initial
        super().__init__(*args, **kwargs)
        self.fields["youtube_url"].label = self.submission.title

    def clean_youtube_url(self):
        from .recording import is_youtube_url

        data = self.cleaned_data["youtube_url"]
        if not is_youtube_url(data):
            raise forms.ValidationError(_("Please provide a youtube.com URL!"))
        return data
