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
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        for item in excluded_paths:
            if path == item or (path + '/') == item:
                return False
            else:
                return True

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
