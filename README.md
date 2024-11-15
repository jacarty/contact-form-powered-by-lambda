# contact-form-powered-by-lambda

This is the code that I used to create the contact form on my website which is hosted on S3.
This approach is a way to get around the static content limitation. 
It uses HTML, Jquery, AWS API Gateway and AWS Lambda. 

Updated to new versions of Bootstrap and Jquery in 2024. 

Notes to get this working: \
1 - You will need to edit the custom.js file and update the URL (line 5) with your API Gateway URL. \
2 - You will need to update the Lambda Function code with your own source and destination Email addresses. \
2a - You will need to put your secret Google key into the Captcha function. \
3 - You should update the Lambda test JSON with a name and an email address. \
4 - You will need to update the HTML code to reflect your google reCAPTCHA Site Key.

Tips for deployment order and testing setup: \
1 - Setup the Lambda function and run the ASW Lambda test to ensure it emails you. \
2 - Setup the API Gateway and use the POST test button to make sure it can talk to Lambda and email you. \
3 - Use a web browser POST plugin (Postman or HttpRequester) to verify your JSON posts to the API Gateway successfully and you get email. \
4 - Now you know your AWS configuration is fine! \
5 - At this point the HTML & Jquery should just work once the API Gateway URL is updated, but if not double check the code for typos...
