"""

Create a context object for the app.

"""
from passlib.context import CryptContext


# Create our context.
pwd_context = CryptContext(
    schemes=['argon2', 'des_crypt'],  # Our hash type
    deprecated='auto',  # Mark all but the first hasher as deprecated.
    )
