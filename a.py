import requests
import random
import string

def generate_random_email(name):
    random_number = ''.join(random.choices(string.digits, k=5))
    return f"{name}{random_number}@gmail.com"

url = "https://formspree.io/mleydddq"

for _ in range(2):
    name = "hacker"
    email = generate_random_email(name)
    message = "hellooo sorry to send "

    data = {
        "name": name,
        "_replyto": email,
        "message": message
    }

    response = requests.post(url, data=data)

    if response.url == "https://formspree.io/thanks?language=en":
        print("Form submitted")
    else:
        print("Failed to submit form")
