from skpy import Skype, SkypeMsg

mail_address = "bot.team1dott@gmail.com"
passwd = "team1dott"

# Dott-Team1
channel_id = "19:f4830852759d4c5f963e11588d888dac@thread.skype"

def post_group_msg():
  
    sk = Skype(mail_address, passwd)

    channel = sk.chats.chat(channel_id)

    # plain-text message
    content = " 3:30 မှာ meeting လုပ်ကြမယ်နော်.."
   
    channel.sendMsg(SkypeMsg.mention_all + content, rich=True)

if __name__ == '__main__':
    post_group_msg()
