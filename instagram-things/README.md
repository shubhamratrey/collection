# Instagram - Stories, Reels, Post, Followers & Followings

## Prerequisites

Add these dependencies before starting anything.

```
requests
math
```

Before staring with anything. Let's start with how to get instagram cookies:

1. Download Chrome
   extension : https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en
2. Login to your instagram account
3. From extension section click on the `editthiscookie` button
4. If you see list of cookies then you're doing it right. Now click on export button (It will copy a list of cookies,
   save it somewhere)

### Get list user ids from available stories.

```
from stories import Stories
cookies = [] (paste the cookies list here)
client = Stories(cookies=cookies, debug=True)
user_ids = client.get_available_stories_user_ids()
print(user_ids)
```

### Get stories from user ids

```
from stories import Stories
cookies = [] (paste the cookies list here)
user_ids = [] (you can use from above list)
client = Stories(cookies=cookies, debug=True)
stories = client.get_stories_using_user_ids(user_ids=user_ids)
print(stories)
```

### Post a photo

```
import urllib.request
img = urllib.request.urlopen('https://instagram.fbho4-1.fna.fbcdn.net/v/t51.2885-19/s320x320/29093337_228763574365850_5571283674877394944_n.jpg?_nc_ht=instagram.fbho4-1.fna.fbcdn.net&_nc_ohc=8-cgeWsuzGMAX8NhY3k&edm=ABfd0MgBAAAA&ccb=7-4&oh=b2ce5cf8af369e33e51942df0f7bd590&oe=60FB15D5&_nc_sid=7bff83')
photo = img.read()
client = Posts(cookies=cookies, debug=True)
result = client.post_a_picture(data=photo, caption="testing. Please Ignore")
print(result)
```

### Post a story

```
import urllib.request
img = urllib.request.urlopen('https://instagram.fbho4-1.fna.fbcdn.net/v/t51.2885-19/s320x320/29093337_228763574365850_5571283674877394944_n.jpg?_nc_ht=instagram.fbho4-1.fna.fbcdn.net&_nc_ohc=8-cgeWsuzGMAX8NhY3k&edm=ABfd0MgBAAAA&ccb=7-4&oh=b2ce5cf8af369e33e51942df0f7bd590&oe=60FB15D5&_nc_sid=7bff83')
photo = img.read()
client = Posts(cookies=cookies, debug=True)
result = client.post_a_story(data=photo, caption="testing. Please Ignore")
```

### Get user's list of reels

```
from stories import Stories
cookies = [] (paste the cookies list here)
user_ids = [] (you can use from above list)
client = Reels(cookies=cookies, debug=True)
post_result = client.get_reels_using_user_id(user_id=1301203788)
print(post_result)
if post_result['max_id']:
   post_result = client.get_reels_using_user_id(user_id=1301203788, max_id=post_result['max_id'])
   print(post_result)
```

### Get follower list of user

```
from followers import Followers
cookies = [] (paste the cookies list here)
client = Followers(cookies=cookies, debug=True)
followers_profiles = client.get_all_followers_profiles_using_user_id(user_id=124)
print(followers_profiles)
```

### Get following list of user

```
from following import Following
cookies = [] (paste the cookies list here)
client = Following(cookies=cookies, debug=True)
following_profiles = client.get_all_following_profiles_using_user_id(user_id=124)
print(following_profiles)
```