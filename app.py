from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv('APP_MESSAGE', 'No message set')
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask DevOps App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                padding: 50px;
                border-radius: 15px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                backdrop-filter: blur(4px);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }}
            h1 {{
                font-size: 3em;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            .message {{
                font-size: 1.5em;
                margin-top: 20px;
                padding: 20px;
                background: rgba(255, 255, 255, 0.2);
                border-radius: 10px;
            }}
            .emoji {{
                font-size: 4em;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">👋🏾</div>
            <h1>Flask DevOps App</h1>
            <div class="message">{message}</div>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    health_status = os.getenv('APP_HEALTH', 'Health status not set')
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Check</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                padding: 50px;
                border-radius: 15px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                backdrop-filter: blur(4px);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }}
            h1 {{
                font-size: 2.5em;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            .status {{
                font-size: 1.5em;
                margin-top: 20px;
                padding: 20px;
                background: rgba(255, 255, 255, 0.2);
                border-radius: 10px;
            }}
            .emoji {{
                font-size: 4em;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">💚</div>
            <h1>Health Check</h1>
            <div class="status">{health_status}</div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)