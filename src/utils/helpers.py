"""
Helper functions used across modules.
"""

import os

def ensure_dir(path):
    """Create directory if it doesn’t exist."""
    os.makedirs(path, exist_ok=True)
