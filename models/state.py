#!/usr/bin/python3
"""Handles the State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    The State Class
    ========================
    Inherits from BaseModel.
    ========================

    Public Class Attributes:
        name: string - empty string

    """
    name = ""

    def to_dict(self):
        """Convert the object's attributes to a dictionary."""
        data = super().to_dict()
        data['name'] = self.name
        return data
