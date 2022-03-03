import instaloader


bot = instaloader.Instaloader()
# profile = instaloader.Profile.from_username(bot.context, 'Rashidov21')
# print(dir(profile))
# print(profile.get_profile_pic_url())

# print("Username: ", profile.username)
# print("User ID: ", profile.userid)
# print("Number of Posts: ", profile.mediacount)
# print("Followers: ", profile.followers)
# print("Followees: ", profile.followees)
# print("Bio: ", profile.biography,profile.external_url)

profile = instaloader.Profile.from_username(bot.context, 'bek_maloy.me')
# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")