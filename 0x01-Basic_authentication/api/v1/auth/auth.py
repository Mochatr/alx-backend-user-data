#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method that returns True if the path is not in the list
        of strings excluded_paths.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Public method that returns None"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method that returns None"""
        return None
