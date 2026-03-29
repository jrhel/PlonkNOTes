import random
import string

def get_session_key():
    pool = string.ascii_letters + string.digits + string.punctuation
    session_key = ""
    while len(session_key) < 32:
        session_key += random.choice(pool)
    return session_key