import json
from client import InstagramClient


class Posts(object):
    DEFAULTS = {
        'preflight-upload': "/rupload_igphoto/fb_uploader_{micro_time}/",
        'upload-post': "/create/configure/",
        'upload-story': "/create/configure_to_story/",
    }

    def __init__(self, cookies, session=None, debug=False):
        self.client = InstagramClient(cookies=cookies, session=session, debug=debug)

    def upload_photo(self, data) -> dict:
        micro_time = self.client.micro_time
        headers = {
            "content-type": "image/jpeg",
            "content-length": "1",
            "x-entity-name": "fb_uploader_{micro_time}".format(micro_time=micro_time),
            "offset": "0",
            "x-entity-length": "1",
            "x-instagram-rupload-params": json.dumps({
                "media_type": 1,
                "upload_id": str(micro_time),
                "upload_media_height": 1080,
                "upload_media_width": 1080
            }),
        }
        resp_json = self.client.post(self.DEFAULTS['preflight-upload'].format(micro_time=micro_time), data=data,
                                     headers=headers)
        return resp_json

    def post_a_picture(self, data, caption):
        """
        Upload photo to Instagram

        :param data: Photo file (String)
        :param caption: Media description (String)
        :return:
        """
        upload_photo_resp = self.upload_photo(data=data)
        upload_id = upload_photo_resp['upload_id']
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR2-43UfYbG2ZZLxh-BQ8N0rqGa-hESkcmxat2RqMAXejXE3',
            'x-instagram-ajax': 'adb961e446b7-hot',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/85.0.4183.121 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': self.client.CSRF_TOKEN,
            'x-ig-app-id': '1217981644879628',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/create/details/',
            'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
        }
        payload = 'upload_id={upload_id}&caption={caption}&usertags=&custom_accessibility_caption=&retry_timeout='.format(
            upload_id=upload_id, caption=caption)
        resp_json = self.client.post(path=self.DEFAULTS['upload-post'], data=payload, headers=headers)
        return resp_json

    def post_a_story(self, data, caption):
        upload_photo_resp = self.upload_photo(data=data)
        upload_id = upload_photo_resp['upload_id']
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR3ZEXbtmat2-n-xCNYMcmuUO3wQxV_TwIkcccquQjq_2h-O',
            'x-instagram-ajax': '894dd5337020',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/'
                          '537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': self.client.CSRF_TOKEN,
            'x-ig-app-id': '1217981644879628',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/create/story/',
            'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
        }

        payload = 'upload_id={upload_id}&caption={caption}'.format(upload_id=upload_id, caption=caption)
        resp_json = self.client.post(self.DEFAULTS['upload-story'], data=payload, headers=headers)
        return resp_json
