import requests
import random
import string

def generate_random_email(name):
    random_number = ''.join(random.choices(string.digits, k=5))
    return f"{name}{random_number}@gmail.com"

url = "https://formspree.io/mleydddq"

# Define user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

for _ in range(2):
    name = "hacker"
    email = generate_random_email(name)
    message = "hellooo sorry to send "

    data = {
        "name": name,
        "_replyto": email,
        "message": message
    }

    headers = {
        "User-Agent": user_agent
    }

    response = requests.post(url, data=data, headers=headers)

    if response.url == "https://formspree.io/thanks?language=en":
        print("Form submitted")
    else:
        print("Failed to submit form")
        
    print("Response Content:")
    print(response.text)
    print(response.url)
