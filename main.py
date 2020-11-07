<<<<<<< HEAD
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
=======
# import json
# from Linebot import LineBotApi
# from Linebot.models import TextSendMessage
>>>>>>> 3c7333b623a4c0314dbb05bb90350e4f663cc8a2

# file = open('info.json', 'r')
# info = json.load(file)

<<<<<<< HEAD
CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

text = ['abcdefg']
text = 2*text
text = '****'.join(text)

def main():
	USER_ID = info['USER_ID']
	messages = TextSendMessage(text=text)
	line_bot_api.push_message(USER_ID, messages=messages)
=======
# CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
# line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# def main():
# 	USER_ID = info['USER_ID']
# 	messages = TextSendMessage(text='hallo')
# 	line_bot_api.push_message(USER_ID, messages=messages)
>>>>>>> 3c7333b623a4c0314dbb05bb90350e4f663cc8a2

# if __name__ == "__main__":
# 	main()

with open('main.py', 'r') as fr:
	rec = fr.read()

with open('abc.txt', 'w') as f:
	f.write('aaa')
