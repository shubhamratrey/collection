import requests
from datetime import datetime


class InstagramClient:
    DEFAULTS = {
        'base_url': 'https://i.instagram.com',
    }

    REQUIRED_COOKIES = ['csrftoken', 'ds_user_id', 'fbm_124024574287414', 'fbsr_124024574287414', 'ig_did', 'ig_nrcb',
                        'mid', 'rur', 'sessionid', 'shbid', 'shbts']

    def __init__(self, cookies, session=None, debug=False):
        self.DEBUG = debug
        self._check_cookies(cookies=cookies)
        self._update_session(cookies=cookies, session=session)

        self.BASE_URL = self.DEFAULTS['base_url']
        if self.DEBUG:
            print()
            for i in self.__dict__:
                print(i, ':', self.__dict__[i])
            print("------")

    def _check_cookies(self, cookies):
        if not cookies:
            raise RuntimeError('Cookies not found')
        AVAILABLE_COOKIES = []
        for cookie_item in cookies:
            name, value = cookie_item['name'], cookie_item['value']
            if name in self.REQUIRED_COOKIES and value:
                AVAILABLE_COOKIES.append(name)
                self._update_properties(name=name, value=value)
        if self.is_debug:
            print("Available Cookies: ", AVAILABLE_COOKIES)
        if len(AVAILABLE_COOKIES) < len(self.REQUIRED_COOKIES):
            missing_cookies = list(filter(lambda x: x not in AVAILABLE_COOKIES, self.REQUIRED_COOKIES))
            raise RuntimeError('Cookies missing: {}'.format(missing_cookies))

    def _update_properties(self, name, value):
        if name == 'csrftoken':
            self.CSRF_TOKEN = value
        elif name == 'ds_user_id':
            self.PROFILE_PRIMARY_KEY = value

    def _update_session(self, cookies, session=None):
        """
        Updates The resource data and header options
        """
        self.SESSION = session or requests.Session()
        for cookie_item in cookies:
            self.SESSION.cookies.set(name=cookie_item['name'],
                                     value=cookie_item['value'],
                                     domain=cookie_item['domain'],
                                     path=cookie_item['path'])

    def _update_user_agent_header(self, options):
        user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
        if 'headers' not in options:
            options['headers'] = {}
        if 'user-agent' not in options['headers']:
            options['headers'].update({'user-agent': user_agent})

        return options

    def _update_request(self, data, options):
        """
        Updates The resource data and header options
        """
        if 'headers' not in options:
            options['headers'] = {}
        if 'content-type' not in options['headers']:
            options['headers'].update({'content-type': 'application/json'})

        return data, options

    def request(self, method, path, **options):
        """
        Dispatches a request to the Instagram HTTP API
        """
        options = self._update_user_agent_header(options)

        url = "{}{}".format(self.BASE_URL, path)

        response = getattr(self.SESSION, method)(url, **options)
        for history_item in response.history:
            if history_item.status_code > 300:
                raise Exception('Invalid Cache. Please update your cache list')

        if (response.status_code >= 200) and (response.status_code < 300):
            return response.json()
        else:
            msg = ""
            code = ""
            json_response = response.json()
            if 'error' in json_response:
                if 'description' in json_response['error']:
                    msg = json_response['error']['description']
                if 'code' in json_response['error']:
                    code = str(json_response['error']['code'])
            raise Exception('Message: {}, Code: {}'.format(msg, code))

    @property
    def is_debug(self):
        return self.DEBUG

    @property
    def base_url(self):
        return str(self.BASE_URL)

    @property
    def csrf_token(self) -> str:
        if not self.CSRF_TOKEN:
            return ''
        return str(self.CSRF_TOKEN)

    @property
    def profile_id(self) -> int:
        if not self.PROFILE_PRIMARY_KEY:
            return 0
        return int(self.PROFILE_PRIMARY_KEY)

    @property
    def micro_time(self):
        return int(datetime.now().timestamp())

    def get(self, path, params, **options):
        """
        Parses GET request options and dispatches a request
        """
        return self.request('get', path, params=params, **options)

    def post(self, path, data, **options):
        """
        Parses POST request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('post', path, data=data, **options)
