# base64_bruteforce
![Title](/Images/base.png)

Many of the ways to log in use different ways to verify your identity. In most cases, systems use a simple login form where you put in your username and password to access the service. In this case, it's easy to brute-force our way into the system by using lists of usernames and passwords. But what happens when these usernames and passwords are filtered?

Some services base64 encode the username and password together and send the base64 encoded username and password over the Authorization request headers.

In this case, I tried to use a general brute-force method in which the username and password are first read from a dictionary. Then it is base64 encoded, and the authorization header uses the encoding to make brute force attacks work.

## Usage
```
python3 /dist/base64_bruteforcy.py [URL] [username.txt] [password.txt]

```

Dependencies:
- The dictionary files should be in txt
- Works for only GET request in this first version
- Install the dependencies using -

```
pip install -r requirements.txt

```

![Title](/Images/flow.jpeg)
