import requests

def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxbac0d563720547e08bfa62651cefa69c.mailgun.org/messages",
        auth=("api", "0458f1a4258f0fcdf581252e5a670159-7caa9475-0cb681f4"),
        data={"from": "Excited User <mailgun@sandboxbac0d563720547e08bfa62651cefa69c.mailgun.org>",
              "to": [email],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})
