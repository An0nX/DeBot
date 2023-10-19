from userbot.src.config import *
from art import text2art


def preinstall():
    print(text2art('SETUP', font='random', chr_ignore=True))
    api_id = int(input('-> [setup] - Введите API ID: '))
    api_hash = input('-> [setup] - Введите API HASH: ')
