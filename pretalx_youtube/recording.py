from pretalx.agenda.recording import BaseRecordingProvider


def is_youtube_url(url):
    return "www.youtube.com/" in url  # TODO better validation


def get_embed_url(url):
    if "www.youtube.com/embed" in url:
        return url
    if not is_youtube_url(url):
        return

    url = url[url.find("www.youtube.com/watch?v=") + len("www.youtube.com/watch?v=") :]
    video_id = url
    return f"https://www.youtube-nocookie.com/embed/{video_id}"

class YouTubeProvider(BaseRecordingProvider):
    def get_recording(self, submission):
        path = self.event.settings.get(f"youtube_url_{submission.code}")
        if not path:
            return
        url = get_embed_url(path)
        if not url:
            return
        iframe = f'<div class="embed-responsive embed-responsive-16by9"><iframe src="{url}" frameborder="0" allowfullscreen></iframe></div>'
        csp_header = "https://www.youtube-nocookie.com"
        return {"iframe": iframe, "csp_header": csp_header}
