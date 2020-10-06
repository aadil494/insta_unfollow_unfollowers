#importing Libraries 
from instabot import Bot 
from time import sleep
from random import randint
import my_config 
#Instantiate the bot object
bot = Bot()
# Login to the instagram account
bot.login(username = my_config.USERNAME,password =my_config.PASSWORD)
# get the followings of our instagram account 
non_followers = set(bot.following) - set(bot.followers)
# Looping over all the users
for non_follower in non_followers:
    try:
        bot.unfollow(non_follower)
        sleep(randint(6,12))
    except Exception as e:
        print(e)
        sleep(randint(30,300))







