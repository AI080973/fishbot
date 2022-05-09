from flask import Flask, request, abort
import random
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
#https://fishsellbot.herokuapp.com/ |
#https://git.heroku.com/fishsellbot.git
app = Flask(__name__)

line_bot_api = LineBotApi('A491ke0DIzg1Ox98+RoDnBWIaAF/21X8xuwJDmGkB0/7oMCca4VBOZiR8AqpMHdB4w2elhqeJjaY45LdnCTHx0q4rK0Xzs5OZZmVp6RDR59ldZtXZm3APASjteYFd2z43vPo0NypEOMA29EBRc/9JQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1267479b2dde12c99bfaea40989e9cd7')#YOUR_LineBot_Channel secret


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.group_id
    print("user_id = ", user_id)      
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=(event.message.text+'\nuser_id: '+user_id)))
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 5000)
