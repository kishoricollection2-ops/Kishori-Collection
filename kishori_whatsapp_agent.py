from flask import Flask, request
import requests, os
app = Flask(__name__)
VERIFY_TOKEN = "kishori_saheli_123"
ACCESS_TOKEN = os.environ.get("WHATSAPP_TOKEN", "YOUR_TOKEN")
PHONE_NUMBER_ID = os.environ.get("PHONE_ID", "1415924871599551")

@app.route("/")
def home():
    return "Kishori Collection WhatsApp Agent is Live! 🙏"

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token")==VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "fail",403

@app.route("/webhook", methods=["POST"])
def webhook():
    data=request.get_json()
    try:
        entry=data['entry'][0]['changes'][0]['value']
        if 'messages' in entry:
            msg=entry['messages'][0]
            frm=msg['from']
            txt=msg['text']['body']
            reply=f"Namaste! Kishori Collection me swagat hai 🙏 Aapne bola: {txt}. Red saree, Suit ya Lehenga chahiye?"
            url=f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"}
            payload={"messaging_product":"whatsapp","to":frm,"type":"text","text":{"body":reply}}
            requests.post(url,json=payload,headers=headers)
    except: pass
    return "OK",200

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
