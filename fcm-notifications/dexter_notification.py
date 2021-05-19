import json
import requests

from oauth2client.service_account import ServiceAccountCredentials
import firebase_admin
from firebase_admin import messaging, credentials


class DexterNotification:

    def __init__(self, service_json, debug=False):
        self.SERVICE_JSON = service_json
        self.PROJECT_ID = service_json['project_id']
        self.BASE_URL = 'https://fcm.googleapis.com'
        self.FCM_ENDPOINT = 'v1/projects/' + self.PROJECT_ID + '/messages:send'
        self.FCM_URL = self.BASE_URL + '/' + self.FCM_ENDPOINT
        self.SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']
        self.DEBUG = debug
        if self.DEBUG:
            print()
            for i in self.__dict__:
                print(i, ':', self.__dict__[i])
            print("------")

    @property
    def service_keyfile_dict(self):
        return self.SERVICE_JSON

    @property
    def is_debug(self):
        return self.DEBUG

    @property
    def fcm_url(self):
        return str(self.FCM_URL)

    @property
    def headers(self):
        bearer_token = self.access_token
        if not bearer_token:
            if self.DEBUG:
                print("EMPTY HEADER")
            return
        return {
            'Authorization': 'Bearer ' + bearer_token,
            'Content-Type': 'application/json; UTF-8',
        }

    @property
    def access_token(self):
        # [START retrieve_access_token]
        """Retrieve a valid access token that can be used to authorize requests.
        :return: Access token.
        """
        cred = self.service_account_credential
        if cred:
            access_token_info = cred.get_access_token()
            return access_token_info.access_token
        else:
            return ''
        # [END use_access_token]

    @property
    def service_account_credential(self):
        """
        :return: ServiceAccountCredentials, a credentials object created from service json
        """
        try:
            return ServiceAccountCredentials.from_json_keyfile_dict(self.SERVICE_JSON, self.SCOPES)
        except (ValueError, KeyError) as e:
            if self.DEBUG:
                print("CREDENTIAL ERROR {}".format(e))
            return None

    def initialize_app_name(self):
        if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
            cred = credentials.Certificate(self.SERVICE_JSON)
            firebase_admin.initialize_app(credential=cred)
            if self.DEBUG:
                print("DEFAULT APP INITIALIZED")
            return True
        else:
            print("DEFAULT APP ALREADY INITIALIZED")
            return True

    def send_single_push_notification(self, data, token):

        """Send HTTP request to FCM with given message.
        :param data: JSON object that will make up the body of the request.
        :param token:
        """

        if not data:
            if self.is_debug:
                print("EMPTY NOTIFICATION DATA")
            return
        if not token:
            if self.is_debug:
                print("EMPTY NOTIFICATION FCM_TOKEN")
            return
        # [START use_access_token]
        headers = self.headers
        if not headers:
            if self.is_debug:
                print("EMPTY HEADER")
            return

        body = {
            "message": {
                "data": data,
                'token': token
            }
        }
        resp = requests.post(self.fcm_url, data=json.dumps(body), headers=headers)
        if resp.status_code == 200:
            if self.is_debug:
                print('Message sent to Firebase for delivery, response:')
                print(resp.text)
            return resp.text
        else:
            if self.is_debug:
                print('Unable to send message to Firebase')
                print(resp.text)
            return resp.text

    def send_multi_push_notifications(self, data, fcm_ids, batch_size=499):
        """
        Create a list containing up to 500 registration tokens.
        These registration tokens come from the client FCM SDKs.
        """
        self.initialize_app_name()

        active_fcm_ids, failure_count = [], 0
        for i in range(0, len(fcm_ids), batch_size):
            batch_tokens = fcm_ids[i:i + batch_size]

            message = messaging.MulticastMessage(android=messaging.AndroidConfig(data=data), tokens=batch_tokens)
            response = messaging.send_multicast(message)

            failure_count += response.failure_count
            active_fcm_ids.extend([batch_tokens[idx] for idx, resp in enumerate(response.responses) if resp.success])
        if self.is_debug:
            print('{0} messages were sent successfully'.format(len(active_fcm_ids)))
