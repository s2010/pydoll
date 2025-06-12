"""
Pydoll Elements Module

This module provides classes for interacting with DOM elements and shadow DOM.
Includes security-focused implementations for element finding and manipulation.
"""

from pydoll.elements.web_element import WebElement
from pydoll.elements.shadow_root import ShadowRoot

__all__ = [
    'WebElement',
    'ShadowRoot',
]
