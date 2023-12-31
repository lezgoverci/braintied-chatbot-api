
from flask import Flask, request, redirect
from flask import jsonify
from dotenv import load_dotenv
from actions.google_calendar import authenticate_google
from actions.openai import add_thread_message, create_run, create_thread, get_thread_last_message, retrieve_run




from api.hubspot import hubspot
from api.messenger import messenger
from api.chat import chat
import os

from tools.openai import create_run_and_get_last_message

load_dotenv()

assistant_id = os.getenv('CHATBOT_OPENAI_ASSISTANT_ID')
server_host = os.getenv('CHATBOT_SERVER_HOST')
server_port = os.getenv('CHATBOT_SERVER_PORT')

app = Flask(__name__)

app.register_blueprint(hubspot, url_prefix='/hubspot')
app.register_blueprint(messenger, url_prefix='/messenger')
app.register_blueprint(chat, url_prefix='/chat')





@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'GET request received!'})

@app.route('/oauth/google', methods=['GET', 'POST'])
def oauth_google():
    # Handle the request here
    service = authenticate_google()
    print(service)
    return redirect('/')




if __name__ == '__main__':
    app.run(host=server_host ,debug=False, port=server_port)
