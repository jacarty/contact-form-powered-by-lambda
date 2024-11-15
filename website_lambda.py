from __future__ import print_function
import boto3, json, urllib, urllib2

ses = boto3.client('ses', region_name='eu-west-1')

def confirm_captcha(captcha):
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': 'XXXXXXX',
        'response': captcha,
    }
    response = urllib2.urlopen(verify_url, urllib.urlencode(payload))
    data = json.load(response)  
    if data['success'] is True:
        return True

def website_email(event, context):
    for each_key, value in event.iteritems():
        if not value.strip():
            return 'Please complete all form fields and try again.'

    captcha = event['g-recaptcha']
    email_from = 'XXXXXXX' 
    email_to = 'XXXXXXX'
    email_reply_address = event['email'].strip()
    email_subject = event['subject'].strip()
    email_body = "Incoming message from {} <{}>\n\n{}".format(event['name'].strip(), 
                                                            event['email'].strip(), 
                                                            event['message'].strip())
    
    try:
        if confirm_captcha(captcha):
            ses.send_email(
                Source = email_from,
                ReplyToAddresses = [email_reply_address],
                Destination={'ToAddresses': [email_to,]},
                Message={
                    'Subject': {'Data': email_subject}, 
                    'Body': {'Text': {'Data': email_body}}
                }
            )
        else:
            return "Captcha was not confirmed. Please try again. Thanks!"
    except:
        return "Hmm something didn't work at the backend. Please try again later. Thanks!"
    else:
        return "Your message has been sent - I'll get back to you soon. Thanks!"