# Signal handlers for third_party_auth app
from django.dispatch import Signal

# Signal fired when a user disconnects a social auth provider account.
# providing_args=["request", "user", "social"]
SocialAuthAccountDisconnected = Signal()
