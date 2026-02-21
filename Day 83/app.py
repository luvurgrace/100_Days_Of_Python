"""
==============================================================================
📊 DATA SCIENCE PORTFOLIO
==============================================================================
"""

from flask import Flask, render_template, request, redirect, url_for, flash, abort
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Import data from config/data.py
from config.data import (
    PERSONAL_INFO,
    STATS,
    SKILLS,
    PROJECTS,
    PROJECT_CATEGORIES
)

# ==============================================================================
# INITIALIZATION
# ==============================================================================

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'fallback-secret-key-change-me')

# Email settings
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER', EMAIL_ADDRESS)  # Where to receive messages


# ==============================================================================
# EMAIL NOTIFICATION
# ==============================================================================

def send_email_notification(name, email, subject, message, contact_method, telegram_username=None):
    """Send email notification about new contact form submission"""

    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        print("⚠️ Email not configured. Check .env file.")
        return False

    try:
        # Create email message
        msg = MIMEMultipart('alternative')
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = f"🌐 Portfolio: {subject or 'New Message'}"

        # Plain text version
        text_content = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📬 NEW MESSAGE FROM YOUR PORTFOLIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 Name: {name}
📧 Email: {email}
📱 Preferred Contact: {contact_method.upper()}
{f'💬 Telegram: {telegram_username}' if telegram_username else ''}
📌 Subject: {subject or 'Not specified'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💬 MESSAGE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """

        # HTML version (prettier in email clients)
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background: linear-gradient(135deg, #4361EE, #7C3AED); color: white; padding: 30px; border-radius: 10px 10px 0 0; text-align: center; }}
        .header h1 {{ margin: 0; font-size: 24px; }}
        .content {{ background: #f9fafb; padding: 30px; border-radius: 0 0 10px 10px; }}
        .info-row {{ display: flex; margin-bottom: 15px; padding: 10px; background: white; border-radius: 8px; }}
        .info-label {{ font-weight: bold; color: #6b7280; min-width: 120px; }}
        .info-value {{ color: #1f2937; }}
        .message-box {{ background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #4361EE; margin-top: 20px; }}
        .message-title {{ font-weight: bold; color: #4361EE; margin-bottom: 10px; }}
        .badge {{ display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }}
        .badge-email {{ background: #dbeafe; color: #1d4ed8; }}
        .badge-telegram {{ background: #cffafe; color: #0891b2; }}
        .footer {{ text-align: center; margin-top: 20px; color: #9ca3af; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📬 New Message</h1>
            <p>Someone contacted you through your portfolio!</p>
        </div>
        <div class="content">
            <div class="info-row">
                <span class="info-label">👤 Name:</span>
                <span class="info-value">{name}</span>
            </div>
            <div class="info-row">
                <span class="info-label">📧 Email:</span>
                <span class="info-value"><a href="mailto:{email}">{email}</a></span>
            </div>
            <div class="info-row">
                <span class="info-label">📱 Contact via:</span>
                <span class="info-value">
                    <span class="badge {'badge-telegram' if contact_method == 'telegram' else 'badge-email'}">
                        {contact_method.upper()}
                    </span>
                </span>
            </div>
            {'<div class="info-row"><span class="info-label">💬 Telegram:</span><span class="info-value">' + telegram_username + '</span></div>' if telegram_username else ''}
            <div class="info-row">
                <span class="info-label">📌 Subject:</span>
                <span class="info-value">{subject or 'Not specified'}</span>
            </div>
            
            <div class="message-box">
                <div class="message-title">💬 Message:</div>
                <p>{message.replace(chr(10), '<br>')}</p>
            </div>
        </div>
        <div class="footer">
            <p>This message was sent from your portfolio contact form</p>
        </div>
    </div>
</body>
</html>
        """

        # Attach both versions
        msg.attach(MIMEText(text_content, 'plain'))
        msg.attach(MIMEText(html_content, 'html'))

        # Send email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"✅ Email sent successfully to {EMAIL_RECEIVER}")
        return True

    except smtplib.SMTPAuthenticationError:
        print("❌ Email authentication failed. Check EMAIL_ADDRESS and EMAIL_PASSWORD.")
        return False
    except smtplib.SMTPException as e:
        print(f"❌ SMTP error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False


# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def get_project_by_id(project_id):
    """Get project by ID"""
    for project in PROJECTS:
        if project['id'] == project_id:
            return project
    return None


def get_featured_projects():
    """Get featured projects for the main page"""
    return [p for p in PROJECTS if p.get('featured', False)]


def get_projects_by_category(category):
    """Get projects filtered by category"""
    if category == 'all':
        return PROJECTS
    return [p for p in PROJECTS if category in p.get('categories', [])]


# ==============================================================================
# CONTEXT FOR ALL TEMPLATES
# ==============================================================================

@app.context_processor
def inject_globals():
    """Variables available in all templates"""
    return {
        'info': PERSONAL_INFO,
        'current_year': datetime.now().year,
    }


# ==============================================================================
# ROUTES
# ==============================================================================

@app.route('/')
def index():
    """Home page"""
    return render_template(
        'index.html',
        stats=STATS,
        skills=SKILLS,
        featured_projects=get_featured_projects(),
    )


@app.route('/projects')
def projects():
    """Projects list page"""
    category = request.args.get('category', 'all')

    return render_template(
        'projects.html',
        projects=get_projects_by_category(category),
        categories=PROJECT_CATEGORIES,
        current_category=category,
    )


@app.route('/projects/<project_id>')
def project_detail(project_id):
    """Project detail page"""
    project = get_project_by_id(project_id)

    if not project:
        abort(404)

    similar = [
        p for p in PROJECTS
        if p['id'] != project_id and
           any(cat in p.get('categories', []) for cat in project.get('categories', []))
    ][:2]

    return render_template(
        'project_detail.html',
        project=project,
        similar_projects=similar,
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with email form"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        contact_method = request.form.get('contact_method', 'email')
        telegram_username = request.form.get('telegram_username', '').strip()

        # Validation
        if not name or not email or not message:
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('contact'))

        # Basic email validation
        if '@' not in email or '.' not in email:
            flash('Please enter a valid email address', 'error')
            return redirect(url_for('contact'))

        # Send email notification
        email_sent = send_email_notification(
            name=name,
            email=email,
            subject=subject,
            message=message,
            contact_method=contact_method,
            telegram_username=telegram_username if contact_method == 'telegram' else None
        )

        # Console output (backup)
        print(f"""
╔══════════════════════════════════════════════════════════╗
║                  📧 NEW MESSAGE                          ║
╠══════════════════════════════════════════════════════════╣
║ Name: {name}
║ Email: {email}
║ Contact Method: {contact_method}
║ Telegram: {telegram_username or 'N/A'}
║ Subject: {subject or 'Not specified'}
║ Message: {message[:100]}{'...' if len(message) > 100 else ''}
║ Email Sent: {'✅ Yes' if email_sent else '❌ No'}
╚══════════════════════════════════════════════════════════╝
        """)

        if email_sent:
            flash('Thank you! Your message has been sent. I\'ll get back to you soon!', 'success')
        else:
            flash('Message received! I\'ll contact you shortly.', 'success')

        return redirect(url_for('contact'))

    return render_template('contact.html')


# ==============================================================================
# ERROR HANDLERS
# ==============================================================================

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


# ==============================================================================
# RUN APPLICATION
# ==============================================================================

if __name__ == '__main__':
    app.run(debug=True, port=5000)