import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Gmail credentials from .env
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USERNAME = os.getenv("SENDER_EMAIL", "").strip()
SMTP_PASSWORD = os.getenv("SENDER_PASSWORD", "").strip()
SENDER_EMAIL = SMTP_USERNAME
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "").strip()

print("🧪 Testing Gmail SMTP Connection...")
print(f"Host: {SMTP_HOST}:{SMTP_PORT}")
print(f"Sender: {SMTP_USERNAME}")
print(f"Recipient: {RECIPIENT_EMAIL}")
print(f"Password length: {len(SMTP_PASSWORD)}")
print("-" * 50)

# Validate credentials are loaded
if not SMTP_USERNAME or not SMTP_PASSWORD or not RECIPIENT_EMAIL:
    print("❌ ERROR: Missing credentials in .env file!")
    print(f"  SENDER_EMAIL: {SMTP_USERNAME if SMTP_USERNAME else 'MISSING'}")
    print(f"  SENDER_PASSWORD: {SMTP_PASSWORD if SMTP_PASSWORD else 'MISSING'}")
    print(f"  RECIPIENT_EMAIL: {RECIPIENT_EMAIL if RECIPIENT_EMAIL else 'MISSING'}")
    print("\nMake sure .env file exists and has all required fields!")
    exit(1)

try:
    print("1️⃣ Connecting to Gmail SMTP...")
    server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
    print("✅ Connected!")
    
    print("2️⃣ Logging in...")
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    print("✅ Login successful!")
    
    print("3️⃣ Creating email message...")
    message = MIMEMultipart("alternative")
    message["From"] = SENDER_EMAIL
    message["To"] = RECIPIENT_EMAIL
    message["Subject"] = "✅ Test Email - Proposal App"
    
    html_body = """
    <html>
        <head>
            <style>
                body { font-family: Arial; text-align: center; padding: 20px; }
                .container { max-width: 600px; margin: 0 auto; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 8px; color: white; }
                h1 { font-size: 28px; margin: 0 0 10px 0; }
                p { font-size: 16px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>✅ GMAIL SMTP TEST SUCCESSFUL!</h1>
                <p>If you're reading this, the Gmail connection is working!</p>
                <p>💕 Proposal App is ready to send emails 💕</p>
            </div>
        </body>
    </html>
    """
    message.attach(MIMEText(html_body, "html"))
    print("✅ Message created!")
    
    print("4️⃣ Sending email...")
    server.send_message(message)
    print("✅ Email sent successfully!")
    
    print("5️⃣ Closing connection...")
    server.quit()
    print("✅ Connection closed!")
    
    print("-" * 50)
    print("🎉 ALL TESTS PASSED!")
    print(f"📧 Check your email: {RECIPIENT_EMAIL}")
    print("   (Check spam folder if not in inbox)")
    
except smtplib.SMTPAuthenticationError as e:
    print(f"❌ AUTHENTICATION FAILED: {e}")
    print("Possible reasons:")
    print("  1. App password is incorrect")
    print("  2. 2FA is not enabled on Gmail")
    print("  3. Password has extra spaces or typos")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    print(f"Error type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
