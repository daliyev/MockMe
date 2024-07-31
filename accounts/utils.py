import hashlib
import os
import binascii
import random


def hash_password(password):
    salt = os.urandom(16)

    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    salt_hex = binascii.hexlify(salt).decode('utf-8')
    hashed_password_hex = binascii.hexlify(hashed_password).decode('utf-8')

    return f'{salt_hex}:{hashed_password_hex}'


def verify_password(password, stored_password):
    salt_hex, hashed_password_hex = stored_password.split(':')

    salt = binascii.unhexlify(salt_hex.encode('utf-8'))
    hashed_password = binascii.unhexlify(hashed_password_hex.encode('utf-8'))

    new_hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    return new_hashed_password == hashed_password


def generate_otp():
    return str(random.randint(10000, 99999))