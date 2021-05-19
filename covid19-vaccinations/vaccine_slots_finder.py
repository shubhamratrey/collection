import requests
from datetime import datetime


class VaccineSlotsFinder:

    def __init__(self, district_id, date=None, debug=False):
        self.DEBUG = debug
        self.BASE_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
        self.DISTRICT_ID = district_id
        self.DATE = date
        self.CENTERS = list()
        self.AGE_AVAILABLE_CAPACITY = {18: 0, 45: 0}
        if self.DEBUG:
            print()
            for i in self.__dict__:
                print(i, ':', self.__dict__[i])
            print("------")
        self.send_request()

    @property
    def is_debug(self):
        return self.DEBUG

    @property
    def base_url(self):
        return str(self.BASE_URL)

    @property
    def params(self):
        if not self.DATE:
            self.DATE = datetime.now().strftime('%d-%m-%y')
        return {'date': self.DATE, 'district_id': self.DISTRICT_ID}

    @property
    def headers(self):
        return {
            'Content-Type': 'application/json; UTF-8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }

    def send_request(self):
        resp = requests.get(url=self.BASE_URL, headers=self.headers, params=self.params)
        if resp.status_code == 200:
            for center in resp.json()['centers']:
                for session in center['sessions']:
                    self.AGE_AVAILABLE_CAPACITY[int(session.get('min_age_limit'))] += session['available_capacity']

    @property
    def is_18_plus_slot_available(self):
        return self.AGE_AVAILABLE_CAPACITY.get(18, 0) > 0

    @property
    def is_45_plus_slot_available(self):
        return self.AGE_AVAILABLE_CAPACITY.get(45, 0) > 0
