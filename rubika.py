import requests
import json
import time

class Robot:
    def __init__(self, auth):
        self.auth = auth
        self.api_url = "https://messengerg2c68.iranlms.ir/"
        self.last_msg_id = 0
        self.handler = None

    def request(self, method, data):
        headers = {"Content-Type": "application/json"}
        payload = {
            "api_version": "5",
            "auth": self.auth,
            "data": data
        }
        try:
            res = requests.post(self.api_url + method, json=payload, headers=headers)
            if res.status_code == 200:
                return res.json()
            else:
                return {"error": res.status_code}
        except Exception as e:
            return {"error": str(e)}

    def send_message(self, chat_id, text, inline_buttons=None):
        data = {
            "peer_guid": chat_id,
            "text": text,
            "reply_to_message_id": "",
        }
        if inline_buttons:
            data["inline_markup"] = {"rows": inline_buttons}
        return self.request("sendMessage", data)

    def get_updates(self):
        return self.request("getMessagesUpdates", {"last_message_id": self.last_msg_id})

    def on_message(self, func):
        self.handler = func

    def run(self):
        print("✅ ربات در حال اجراست...")
        while True:
            updates = self.get_updates()
            if "updates" in updates:
                for update in updates["updates"]:
                    if update["type"] == "Message":
                        self.last_msg_id = update["message_id"]
                        if self.handler:
                            self.handler(update)
            time.sleep(1)