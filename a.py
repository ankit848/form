import requests
import random
import string
from fake_useragent import UserAgent

def generate_random_email(name):
    random_number = ''.join(random.choices(string.digits, k=5))
    return f"{name}{random_number}@gmail.com"

url = "https://formspree.io/mleydddq"

for _ in range(100000):
    name = "hackerdona"
    email = generate_random_email(name)
    message = "Hellooo sorry to send hehe "

    data = {
        "name": name,
        "_replyto": email,
        "message": message
    }

    # Generate a random user agent
    user_agent = UserAgent().random
    headers = {
        "User-Agent": user_agent
    }

    response = requests.post(url, data=data, headers=headers)

    if response.url == "https://formspree.io/thanks":
        print("Form submitted")
    else:
        print("Failed to submit form")
        print(response.url)
