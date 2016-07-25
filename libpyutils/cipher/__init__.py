#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid1
from hashlib import sha512, sha256, md5
from base64 import b64encode, b64decode

import bcrypt


def __by_hashlib(algo, plain_text):
    return getattr(hashlib, algo)(plain_text).hexdigest()


def hash_md5(plain_text):
    return __by_hashlib('md5', plain_text)


def hash_sha512(plain_text):
    return __by_hashlib('sha512', plain_text)


def hash_sha256(plain_text):
    return __by_hashlib('sha256', plain_text)


def passwd_encrypt(plain_passwd):
    """encrypt plain password by BCrypt Algorithem
    """
    return bcrypt.hashpw(plain_passwd, bcrypt.gensalt())


def check_passwd(plain_passwd, encypt_passwd):
    """decrypt hashed password by BCrypt Algorithem
    """
    return bcrypt.checkpw(plain_passwd, encypt_passwd)


def gen_uuid():
    return str(uuid1())

