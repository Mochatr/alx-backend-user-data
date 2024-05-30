#!/usr/bin/env python3
"""
This module provides the filter_datum function
to obfuscate specific fields in a log message.
"""

import logging
import mysql.connector
import os
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    logger = logging.getLoger("user_data")
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MYSQLConnection:
    """Returns a connector to the database"""
    host = os.getenv('PERSONAL_DATA_DB_HOST') or 'localhost'
    user = os.getenv('PERSONAL_DATA_DB_USERNAME') or 'root'
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ''
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=database
    )


def main() -> None:
    """
    Acquire a database connection using get_db and retrieve all rows
    in the users table and display each row under a filtered format
    """
    logger = get_logger()
    connector = get_db()

    cursor = connector.cursor()
    cursor.execute('SELECT * FROM `users`;')

    users = cursor.column_names
    column_names = cursor.column_names

    for user in users:
        formatted_user = "".join(f"{attribute}={value}; " for
                                 attribute, value in zip(column_names, user))
        logger.info(formatted_user)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with the fields to be
        redacted.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by redacting sensitive fields.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


if __name__ == "__main__":
    main()
