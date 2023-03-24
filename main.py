import sys
import time
import telepot
from telepot.loop import MessageLoop
import requests
import json

teleToken="5677511232:AAE3Yt4lO4zEzXg3_olMaCHo1tt3-muYxHE"
api_url="https://api.openai.com/v1/chat/completions"
api_token="Bearer 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"

def toChatgpt(msg):
    payload = json.dumps({
        "model": "gpt-3.5-turbo-0301",
        "temperature": 0.7,
        "messages": [
            {
                "role": "user",
                "content": "give me hello world code exam"
            }
        ]
    })
    headers = headers = {'Authorization': api_token,'Content-Type': 'application/json'}
    response = requests.post(api_url, data=payload, headers=headers)
    response.raise_for_status()

    res = json.loads(response.text)
    #text =
    return res['choices'][0]['message']['content']
    
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg['text'])

    if content_type == 'text':
        res = toChatgpt(msg['text'])
        bot.sendMessage(chat_type,res)


bot = telepot.Bot(teleToken)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
