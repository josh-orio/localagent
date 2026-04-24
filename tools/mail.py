import resend
import os

def notify(to: str, subject: str, body: str) -> None:
    """Send user notification email.

    Args:
        to: Email address
        subject: Subject line
        body: Main content (plain text)

    Returns:
        None
    """

    resend.api_key = os.environ["RESEND_API_KEY"]

    r = resend.Emails.send({
    "from": "agent-notif@resend.dev",
    "to": to,
    "subject": subject,
    "text": body.encode('utf-8').decode('unicode_escape').encode('latin-1').decode('utf-8'),
    })

__all__ = ["notify"]
