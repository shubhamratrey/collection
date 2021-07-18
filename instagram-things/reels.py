from client import InstagramClient
import math


class Reels(object):
    DEFAULTS = {
        'reel_tray': "/api/v1/clips/user/",
    }

    def __init__(self, cookies, session=None, debug=False):
        self.client = InstagramClient(cookies=cookies, session=session, debug=debug)

    def get_reels_using_user_id(self, user_id, page_size=12, max_id=None):
        """
        :param page_size:
        :param user_id:
        :param max_id:
        :return:
        """
        headers = {
            'authority': 'www.instagram.com',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
            'x-csrftoken': self.client.CSRF_TOKEN,
            'x-ig-app-id': '1217981644879628',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/',
            'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
        }
        payload = {
            'target_user_id': user_id,
            'page_size': page_size,
            'max_id': max_id
        }
        data = {}
        resp_json = self.client.post(self.DEFAULTS['reel_tray'], data=payload, headers=headers)
        if resp_json['status'] != 'ok':
            return data
        data.update({
            'items': [],
            'has_more': resp_json['paging_info']['more_available'],
            'max_id': resp_json['paging_info']['max_id']
        })
        for media_data in resp_json['items']:
            media_item = media_data['media']
            data['items'].append({
                'like_count': media_item['like_count'],
                'view_count': media_item['view_count'],
                'play_count': media_item['play_count'],
                'comment_count': media_item['comment_count'],
                'caption': media_item['caption']['text'],
                'video_url': media_item['video_versions'][0]['url'],
                'image_url': media_item['image_versions2']['candidates'][0]['url'],
            })
        return data
