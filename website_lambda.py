from __future__ import print_function
import json
import boto3

ses = boto3.client('ses', region_name='eu-west-1') #region must be SES enabled

def website_email(event, context):
    if not event['name'].strip():
        return 'Please enter your name.'
    elif not event['email'].strip():
        return 'Please provide your email address.'
    elif not event['subject'].strip():
        return 'Please add a subject.'
    elif not event['message'].strip():
        return 'Did you forget a message?'

    email_from = 'UPDATE WITH YOUR ADDRESS' #Must be validated with AWS or SES will return an error
    email_to = 'UPDATE WITH YOUR ADDRESS' #Destination email address
    email_subject = event['subject'].strip()
    email_reply_address = event['email'].strip()
    email_body = "Incoming message from {} <{}>\n\n{}".format(event['name'].strip(), event['email'].strip(), event['message'].strip())

    try:
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
    except:
        return "Hmm something didn't work. Please try again. Thanks!"
    else:
        return "Your message has been sent - I'll get back to you soon. Thanks!"