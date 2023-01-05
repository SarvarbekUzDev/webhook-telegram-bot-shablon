import json
import requests


class Sends:
    """
    Telegram bot sends. 
    Sends all methods:
        send_message,
        send_photo,
        send_video,
        send_audio,
        send_document,
        send_media.
    ----- PARSE MODE -------
        <b>bold</b>,
        <strong>bold</strong>
        <i>italic</i>,
        <em>italic</em>
        <a href="URL">inline URL</a>
        <code>inline fixed-width code</code>
        <pre>pre-formatted fixed-width code block</pre>
    """
    def __init__(self, token):
        self.token = token
            
    # Send Message
    def send_message(self, chat_id, text, reply_markup=None, variable_name=None):
        method = "sendMessage"
        url_req = "https://api.telegram.org/bot" + self.token + f"/{ method }"
        data =  {"chat_id":str(chat_id), "text":text, "parse_mode":"HTML",
                    "reply_markup": json.dumps(reply_markup[f"{variable_name}"] if reply_markup else {})}
        results = requests.post(url_req, data=data)

        return results


    # Send Photo
    def send_photo(self, chat_id, photo, caption=None, reply_markup=None, variable_name=None):
        method = "sendPhoto"
        url_req = 'https://api.telegram.org/bot' + self.token + f'/{ method }'
        data = {"chat_id":chat_id, "photo":photo, "caption":caption, "parse_mode":"HTML",
                "reply_markup":json.dumps(reply_markup[f"{variable_name}"] if reply_markup else {})}

        results = requests.post(url_req, data=data)

        return results


    # Send Video
    def send_video(self, chat_id, video, caption=None, reply_markup=None, variable_name=None):
        method = "sendVideo"
        url_req = 'https://api.telegram.org/bot' + self.token + f'/{ method }'
        data = {"chat_id":chat_id, "video":video, "caption":caption, "parse_mode":"HTML",
                "reply_markup":json.dumps(reply_markup[f"{variable_name}"] if reply_markup else {})}

        results = requests.post(url_req, data=data)

        return results


    # Send Audio
    def send_audio(self, chat_id, audio, caption=None, reply_markup=None, variable_name=None):
        method = "sendAudio"
        url_req = 'https://api.telegram.org/bot' + self.token + f'/{ method }'
        data = {"chat_id":chat_id, "audio":audio, "caption":caption, "parse_mode":"HTML",
                "reply_markup":json.dumps(reply_markup[f"{variable_name}"] if reply_markup else {})}

        results = requests.post(url_req, data=data)

        return results


    # Send Document
    def send_document(self, chat_id, document, caption=None, reply_markup=None, variable_name=None):
        method = "sendDocument"
        url_req = 'https://api.telegram.org/bot' + self.token + f'/{ method }'
        data = {"chat_id":chat_id, "document":document, "caption":caption, "parse_mode":"HTML",
                "reply_markup":json.dumps(reply_markup[f"{variable_name}"] if reply_markup else {})}

        results = requests.post(url_req, data=data)

        return results


    # Send Media
    def send_media(self, chat_id, media, reply_markup=None, variable_name=None):
        method = "sendMediaGroup"
        url_req = 'https://api.telegram.org/bot' + self.token + f'/{ method }'

        # [{"type":"photo","media":media, "caption":caption}]
        media = json.dumps(media)
        data = {"chat_id":chat_id, "media":media, "parse_mode":"HTML",
                "reply_markup":json.dumps(reply_markup[f"{variable_name}"] if reply_markup else {})}
        results = requests.post(url_req, data=data)

        return results
