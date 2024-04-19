#!/usr/bin/env python3
"""
manages the api authentication
"""
from flask import request
from typing import List, TypeVar
import fnmatch


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
            if fnmatch.fnmatch(path, item):
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """
        validates all requests to validate the API
        """
        header = request.headers.get('Authorization')
        if header is None or request is None:
            return None
        else:
            return header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns none
        """
        return None

    def session_cookie(self, request=None):
        """
        """

        if request is None:
            return None
        session = os.getenv('SESSION_NAME')
        return request.cookie.get(session)
