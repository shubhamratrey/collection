# Send Firebase Cloud Messaging notifications

## Prerequisites

Add these dependencies before starting anything.

```groovy
oauth2client
firebase_admin
requests
```

[comment]: <> (To learn how to get started with Cloud Functions for Firebase by having a look at)

[comment]: <> (our [Getting Started Guide]&#40;https://firebase.google.com/docs/functions/get-started&#41;, trying)

[comment]: <> (the [quickstart samples]&#40;/quickstarts&#41; and looking at [the documentation]&#40;https://firebase.google.com/docs/functions&#41;.)

### Initialize Notification

```
from .dexter_notification import DexterNotification
dn = DexterNotification(service_json={
    "type": "service_account",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "",
    "client_x509_cert_url": ""
}, debug=True)

```

### Send Notification to single device

```
dn.send_single_push_notification(
    data={
        'title': "We'll remind you once vaccine is available",
        'description': 'Successfully registered for {date} vacc'
    },
    token='fPN8VSQER3CFgLxPeWi5x8:APA91bF4ccwqbxtYD67vvpzADV3mzWVLslOrn5GWO5MT7qx9VBjdT_npsMLSCr4V_4jTLP0zrA6a0KAbPySZgnBzU8NgYsqWuzAuOnucoZCsbrBLSo46JuXhAh_Mp8Tn6foKw5SiG2x3')
```

### Send Notification to multiple device

```
dn.send_multi_push_notifications(data={
    'title': "We'll remind you once vaccine is available",
    'description': 'Successfully registered for {date} vacc'
}, fcm_ids=[
    'fPN8VSQER3CFgLxPeWi5x8:APA91bF4ccwqbxtYD67vvpzADV3mzWVLslOrn5GWO5MT7qx9VBjdT_npsMLSCr4V_4jTLP0zrA6a0KAbPySZgnBzU8NgYsqWuzAuOnucoZCsbrBLSo46JuXhAh_Mp8Tn6foKw5SiG2x3',
    'fPN8VSQER3CFgLxPeWi5x8:APA91bF4ccwqbxtYD67vvpzADV3mzWVLslOrn5GWO5MT7qx9VBjdT_npsMLSCr4V_4jTLP0zrA6a0KAbPySZgnBzU8NgYsqWuzAuOnucoZCsbrBLSo46JuXhAh_Mp8Tn6foKw5SiG2x3'])

```

