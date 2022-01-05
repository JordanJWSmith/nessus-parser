import hashlib
import logging
import requests

def hash_file(file):
    try:
        logging.info('hash_file')
        hasher = hashlib.md5()
        buf = file.read()
        hasher.update(buf)
        logging.info(hasher.hexdigest())
    except Exception as e:
        return e
    return hasher.hexdigest()
    

def file_list():
    res = requests.get('http://localhost:8000/file-hashes/')
    return res.json()['data']
