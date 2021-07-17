from client import InstagramClient
import math


class Reels(object):
    DEFAULTS = {
        'reel_tray': "/feed/reels_tray/",
        'reels_media': "/feed/reels_media/"
    }

    def __init__(self, cookies, session=None, debug=False):
        self.client = InstagramClient(cookies=cookies, session=session, debug=debug)

    def get_available_reels_user_ids(self, filter_user_ids=[], **kwargs):
        """
        Parses GET request options and dispatches a request
        """

        resp_json = self.client.get(self.DEFAULTS['reel_tray'], params={}, **kwargs)
        tray_list = resp_json.get('tray', {})
        reel_ids = []
        for reel_item in tray_list:
            print(reel_item)
            user_dict = reel_item['user']
            if filter_user_ids:
                if user_dict['pk'] in filter_user_ids:
                    reel_ids.append(reel_item['id'])
                else:
                    pass
            else:
                reel_ids.append(reel_item['id'])
        return reel_ids

    def get_reels_using_user_ids(self, user_ids, page_size=25, **kwargs):
        """
        :param page_size:
        :param user_ids:
        :return: {
            'seemantsingh3': {
                'username': 'seemantsingh3',
                'full_name': 'Seemant Singh',
                'profile_pic_url': 'https://instagram.fbho4-1.fna.fbcdn.net/v/t51.2885-19/s150x150/69689857_2308637486063763_5158324914419138560_n.jpg?_nc_ht=instagram.fbho4-1.fna.fbcdn.net&_nc_ohc=GlNIoJ5Yd7QAX9x93F7&edm=ANmP7GQBAAAA&ccb=7-4&oh=c453dcde74506aeec601966f1fab22aa&oe=60F41C8A&_nc_sid=276363',
                'video_reels': ['https://instagram.fbho4-2.fna.fbcdn.net/v/t66.30100-16/46858200_411330083460145_6407877835166960223_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLjY0MC5zdG9yeS5jb250cm9sLWItYmFzZWxpbmUiLCJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSJ9&_nc_ht=instagram.fbho4-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=hUi5Y_BwMFMAX_dPGZ0&edm=ANmP7GQBAAAA&vs=802648820440966_3491458815&_nc_vs=HBksFQAYJEdOai15Z0l4bElJLUduWUJBRi1LT2RId1d1MVlicFIxQUFBRhUAAsgBABUAGCRHQXR6X2d5d3R5M2FyT0lDQURtUVAyYkw1WU40YnBrd0FBQUYVAgLIAQAoABgAGwGIB3VzZV9vaWwBMRUAACawo6ei%2BanWPxUCKAJDMywXQC3ul41P3zsYHGRhc2hfY29udHJvbC1iLWJhc2VsaW5lXzFfdjERAHXoBwA%3D&ccb=7-4&oe=60EEF68C&oh=a5ee27c9be6ae1b0e1ff52728b9496fd&_nc_sid=276363'],
                'image_reels': []
            }
        }
        """
        data = {}
        n_pages = math.ceil((len(user_ids) + 1) / page_size)

        start_index, end_index = 0, page_size
        page_index = 1
        while page_index <= n_pages:
            page_index += 1
            params = {'reel_ids': user_ids[start_index:end_index]}
            resp_json = self.client.get(self.DEFAULTS['reels_media'], params=params, **kwargs)
            reels = resp_json.get('reels', {})
            for reel_id in reels:
                reel = reels.get(str(reel_id), {})
                user = reel.get('user', {})
                if not data.get(user.get('username', ''), None):
                    data[user.get('username', '')] = {
                        'pk': user.get('pk', ''),
                        'username': user.get('username', ''),
                        'full_name': user.get('full_name', ''),
                        'profile_pic_url': user.get('profile_pic_url', ''),
                        'video_reels': [],
                        'image_reels': []
                    }

                for item in reel.get('items', []):
                    if len(item.get('video_versions', [])) > 0:
                        video_url = item.get('video_versions', [])[0].get('url', '')
                        data[user.get('username', '')].get('video_reels').append({
                            'url': video_url,
                            'id': item['pk']
                        })
                    elif len(item.get('image_versions2', {}).get('candidates', [])) > 0:
                        image_url = item.get('image_versions2', {}).get('candidates', [])[0].get('url', '')
                        data[user.get('username', '')].get('image_reels').append({
                            'url': image_url,
                            'id': item['pk']
                        })

            start_index = end_index
            end_index += page_size
        return data
