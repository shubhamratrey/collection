cookies = [

]

from reels import Reels

if __name__ == '__main__':
    insta_reels = Reels(cookies=cookies, debug=True)
    reels_ids = insta_reels.get_available_reels_user_ids(filter_user_ids=[642735754, 18660730])
    print(reels_ids)
    reels_media = insta_reels.get_reels_using_user_ids(user_ids=[642735754, 18660730])
    print(reels_media)
