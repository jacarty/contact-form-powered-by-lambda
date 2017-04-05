from __future__ import print_function
import boto3, json, urllib, urllib2

ses = boto3.client('ses', region_name='eu-west-1')

def confirm_captcha(captcha):
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': 'XXXXXX',
        'response': captcha,
    }
    response = urllib2.urlopen(verify_url, urllib.urlencode(payload))
    data = json.load(response)  
    if data['success'] is True:
        return True

def website_email(event, context):
    if not event['name'].strip():
        return 'Please enter your name.'
    elif not event['email'].strip():
        return 'Please provide your email address.'
    elif not event['subject'].strip():
        return 'Please add a subject.'
    elif not event['message'].strip():
        return 'Did you forget a message?'

    email_from = 'XXXXXX' 
    email_to = 'XXXXXX'
    email_subject = event['subject'].strip()
    email_reply_address = event['email'].strip()
    email_body = "Incoming message from {} <{}>\n\n{}".format(event['name'].strip(), event['email'].strip(), event['message'].strip())
    captcha = event['g-recaptcha']
    
    try:
        if confirm_captcha(captcha):
            ses.send_email(
                Source = email_from,
                ReplyToAddresses = [email_reply_address],
                Destination={
                    'ToAddresses': [
                        email_to,
                    ],
                },
                Message={
                    'Subject': {
                        'Data': email_subject
                    },
                    'Body': {
                        'Text': {
                            'Data': email_body
                        }
                    }
                }
            )
        else:
            return "Captcha was not confirmed. Please try again. Thanks!"
    except:
        return "Hmm something didn't work at the backend. Please try again later. Thanks!"
    else:
        return "Your message has been sent - I'll get back to you soon. Thanks!"
        
#Lambda Test JSON

#{
#    "name": "Your Name",
#    "email": "Your Email Address",
#    "subject": "hi",
#    "message": "lambda is working",
#    "g-recaptcha": "this will fail the test"
#}