import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Gmail SMTP Configuration
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USERNAME = os.getenv("SENDER_EMAIL", "").strip()
SMTP_PASSWORD = os.getenv("SENDER_PASSWORD", "").strip()

# Email recipients
SENDER_EMAIL = SMTP_USERNAME
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "shashankhsg@gmail.com").strip()

# Debug output
print(f"✓ Gmail SMTP: {SMTP_HOST}:{SMTP_PORT}")
print(f"✓ Sender Email: {SENDER_EMAIL}")
print(f"✓ Recipient Email: {RECIPIENT_EMAIL}")

def send_email(subject: str, body: str):
    """
    Send HTML email using Gmail SMTP service
    """
    try:
        print(f"📧 Sending email: {subject}")
        
        # Create message
        message = MIMEMultipart("alternative")
        message["From"] = SENDER_EMAIL
        message["To"] = RECIPIENT_EMAIL
        message["Subject"] = subject
        
        # Attach HTML body
        html_body = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 8px; }}
                    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px 8px 0 0; text-align: center; }}
                    .header h1 {{ margin: 0; font-size: 28px; }}
                    .content {{ background: white; padding: 30px; border-radius: 0 0 8px 8px; }}
                    .message {{ font-size: 16px; color: #555; }}
                    .heart {{ color: #e91e63; font-size: 24px; }}
                    .footer {{ text-align: center; margin-top: 20px; font-size: 12px; color: #999; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>💕 Proposal App Response 💕</h1>
                    </div>
                    <div class="content">
                        <p class="message">{body}</p>
                        <p class="heart">❤️ 💖 💗 💝</p>
                    </div>
                    <div class="footer">
                        <p>This email was sent from the Proposal App</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        message.attach(MIMEText(html_body, "html"))
        
        # Connect to Gmail SMTP server with SSL
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(message)
        
        print(f"✅ Email sent successfully: {subject}")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        return False