from instabot import Bot

bot = Bot()
bot.login( username = "", password = "")
bot.follow(' Enter the name of account that you want to follow')
bot.upload_photo(" specify the path", caption = "I am doing python")
bot.unfolloq(" Enter the name of account")

bot.send_message("We doing python", ["enter account name 1" , "Enter account name 2"])

followers = bot.get_user_followers("your account name")

for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("your account name")

for Following in following:
    print(bot.get_user_info(following))
