#!/usr/bin/python3
"""
This module contains storage, an instance of the FileStorage class
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
