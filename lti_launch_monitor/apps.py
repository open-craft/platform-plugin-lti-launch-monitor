"""
lti_launch_monitor Django application initialization.
"""

from django.apps import AppConfig


class LtiLaunchMonitorConfig(AppConfig):
    """
    Configuration for the lti_launch_monitor Django application.
    """

    name = "lti_launch_monitor"

    plugin_app = {}

    def ready(self):
        """
        LTI Launch Monitor application initialization.
        """
        from lti_launch_monitor import signal_handlers  # pylint: disable=unused-import,import-outside-toplevel
