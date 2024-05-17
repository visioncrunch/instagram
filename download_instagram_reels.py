import os
from instaloader import Instaloader, Profile

bot = Instaloader(
    download_pictures=False,         # Disable downloading pictures
    download_videos=True,            # Enable downloading videos
    download_video_thumbnails=False, # Disable downloading video thumbnails
    download_geotags=False,          # Disable downloading geotags
    download_comments=False,         # Disable downloading comments
)

username = "your_username"
password = "your_password"
bot.login(username,password)
print(bot.download_saved_posts())