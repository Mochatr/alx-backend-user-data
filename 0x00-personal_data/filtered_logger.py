#!/usr/bin/env python3
"""
This module provides the filter_datum function
to obfuscate specific fields in a log message.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): String to replace the field values with.
        message (str): Log message to be processed.
        separator (str): Character separating the fields in the log message.

    Returns:
        str: The log message with obfuscated field values.
    """
    return re.sub(rf'({"|".join(fields)})=.*?{separator}',
                  lambda m: f"{m.group(1)}={redaction}{separator}", message)
