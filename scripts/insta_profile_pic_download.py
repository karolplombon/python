# Works on Python 3.10.4
# Before running script install following
# pip3 install instaloader

import instaloader
bot = instaloader.Instaloader()
username = 'username'
print(bot.download_profile(username, profile_pic_only=True))
