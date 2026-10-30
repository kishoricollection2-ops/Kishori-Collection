from flask import Flask, request
import requests, os
app = Flask(__name__)
VERIFY_TOKEN = "kishori_saheli_123"
ACCESS_TOKEN = os.environ.get("WHATSAPP_TOKEN", "TOKEN")
PHONE_NUMBER_ID = os.environ.get("PHONE_ID", "1456262570898256")
@app.route("/webhook", methods=["GET"])
def verify():
 if request.args.get("hub.verify_token")==VERIFY_TOKEN:
  return request.args.get("hub.challenge")
 return "fail",403
@app.route("/webhook", methods=["POST"])
def webhook():
 return "OK",200
if __name__=="__main__":
 app.run(host="0.0.0.0",port=5000)
