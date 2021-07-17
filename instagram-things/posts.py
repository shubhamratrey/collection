from client import InstagramClient


class Posts(object):
    DEFAULTS = {
        'reel_tray': "/feed/reels_tray/",
        'reels_media': "/feed/reels_media/"
    }

    def __init__(self, cookies, session=None, debug=False):
        self.client = InstagramClient(cookies=cookies, session=session, debug=debug)

    def post_a_picture(self, **kwargs):
        """
        Parses GET request options and dispatches a request
        """
        resp_json = self.client.post(self.DEFAULTS['reel_tray'], params={}, **kwargs)
        return resp_json
