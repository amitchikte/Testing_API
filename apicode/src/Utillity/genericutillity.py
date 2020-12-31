import logging as logger
import random
import string


def random_email_and_password(domain = None,email_prefix= None):
    if not domain:
        domain = "gmail.com"
    if not email_prefix:
        email_prefix = "testuser"

    random_string_len = 10
    random_string = ''.join((random.choices(string.ascii_lowercase,k=random_string_len)))
    print(random_string)
    email = email_prefix + random_string +"@"+domain
    print(email)

    password_len = 15
    password_string = ''.join(random.choices(string.ascii_lowercase,k=password_len))
    print(password_string)

    random_info = {"email":email,"password":password_string}
    logger.debug(f"randomly generated email & password is {random_info}")

    return random_info


print(random_email_and_password("gmail.com","amit"))