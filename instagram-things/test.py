from stories import Stories
from posts import Posts
from reels import Reels
from followers import Followers
from following import Following
import urllib.request

cookies = []
if __name__ == '__main__':
    # Get list user ids from available stories.
    client = Stories(cookies=cookies, debug=True)
    user_ids = client.get_available_stories_user_ids()
    print(user_ids)

    # Get stories from user ids
    client = Stories(cookies=cookies, debug=True)
    stories = client.get_stories_using_user_ids(user_ids=user_ids)
    print(stories)

    # Get Followers from user id
    client = Followers(cookies=cookies, debug=True)
    followers_profiles = client.get_all_followers_profiles_using_user_id(user_id=124)
    print(followers_profiles)

    # Get Followings from user id
    client = Following(cookies=cookies, debug=True)
    following_profiles = client.get_all_following_profiles_using_user_id(user_id=124)
    print(following_profiles)

    img = urllib.request.urlopen(
        'https://instagram.fbho4-1.fna.fbcdn.net/v/t51.2885-19/s320x320/29093337_228763574365850_5571283674877394944_n.jpg?_nc_ht=instagram.fbho4-1.fna.fbcdn.net&_nc_ohc=8-cgeWsuzGMAX8NhY3k&edm=ABfd0MgBAAAA&ccb=7-4&oh=b2ce5cf8af369e33e51942df0f7bd590&oe=60FB15D5&_nc_sid=7bff83')
    photo = img.read()

    # Post a photo
    client = Posts(cookies=cookies, debug=True)
    post_result = client.post_a_picture(data=photo, caption="testing. Please Ignore")
    print(post_result)

    # Post a story
    client = Posts(cookies=cookies, debug=True)
    story_result = client.post_a_story(data=photo, caption="testing. Please Ignore")
    print(story_result)

    # Get a User Reels
    client = Reels(cookies=cookies, debug=True)
    post_result = client.get_reels_using_user_id(user_id=1301203788)
    print(post_result)
    if post_result['max_id']:
        post_result = client.get_reels_using_user_id(user_id=1301203788, max_id=post_result['max_id'])
        print(post_result)
