#!/usr/bin/env python3
"""
"""
import bcrypt


def hash_password(pass: str) -> bytes:
    """
    """
    return bcrypt.hashpw(pass.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed: bytes, pass: str) -> bool:
    """
    """
    return bcrypt.checkpw(pass.encode('utf-8'), hashed)
