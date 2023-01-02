from instabot import Bot
import time
bot=Bot()
bot.login(username="",password="")

'bot.follow("priyanshu_batham_1")'
'print("followed successfully")'



'''bot.like_user(user_id="priyanshu_batham_1",filtration= False)
print("Likeddddd")'''

bot.follow_following(user_id="priyanshu_batham_1")


'''a=bot.get_user_following(user_id="priyanshu_batham_1",nfollows=5)
b=[]
for i in a:
    b.append(bot.get_username_from_user_id(i))
print(b)'''




