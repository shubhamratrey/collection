from client import InstagramClient


class Following(object):
    DEFAULTS = {
        'following': "/api/v1/friendships/{user_id}/following/",
    }

    def __init__(self, cookies, session=None, debug=False):
        self.client = InstagramClient(cookies=cookies, session=session, debug=debug)

    def get_all_following_profiles_using_user_id(self, user_id):
        data = {
            'users': [],
            'n_request': 0,
            'count': 0
        }
        looping = True
        next_max_id = None
        while looping:
            inner_users, next_max_id = self.get_following_profiles_using_user_id(user_id=user_id,
                                                                                 next_max_id=next_max_id)
            if inner_users:
                data['users'].extend(inner_users)
                data['n_request'] += 1
            if not next_max_id:
                looping = False
        data['count'] = len(data['users'])
        return data

    def get_following_profiles_using_user_id(self, user_id, next_max_id=None, page_size=200):
        users, max_id = [], None
        params = {'max_id': next_max_id, 'count': page_size} if next_max_id else {'count': page_size}
        resp_json = self.client.get(self.DEFAULTS['following'].format(user_id=user_id), params=params)
        if resp_json['status'] != 'ok':
            return users
        for user_item in resp_json['users']:
            users.append({
                'pk': user_item['pk'],
                'username': user_item['username'],
                'is_private': user_item['is_private'],
                'profile_pic_url': user_item['profile_pic_url'],
                'is_verified': user_item['is_verified'],
            })
        max_id = resp_json.get('next_max_id', None)
        return users, max_id
