#!/usr/bin/env python3
"""
manages the api authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    a class to manage the api
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns a boolean
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        returns none
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns none
        """
        return None
