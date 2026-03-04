# lint-amnesty, pylint: disable=missing-module-docstring

from django.apps import AppConfig


class ThirdPartyAuthConfig(AppConfig):  # lint-amnesty, pylint: disable=missing-class-docstring
    name = 'common.djangoapps.third_party_auth'
    verbose_name = "Third-party authentication"

    def ready(self):
        from .signals import handlers  # noqa: F401 pylint: disable=unused-import
