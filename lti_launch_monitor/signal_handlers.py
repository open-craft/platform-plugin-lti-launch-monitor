"""
Signal handlers for lti_launch_monitor.
"""

from django.contrib.auth import get_user_model
from openedx_events.learning.data import LtiProviderLaunchData
from openedx_events.learning.signals import LTI_PROVIDER_LAUNCH_SUCCESS

from lti_launch_monitor.models import LTILaunchRecord

User = get_user_model()


def record_lti_provider_launch_success(launch_data: LtiProviderLaunchData | None = None, **kwargs):
    """
    Record a successful LTI launch in the database.
    """
    if launch_data:
        extra_params = launch_data.launch_params.extra_params.copy()
        extra_params["roles"] = launch_data.launch_params.roles
        extra_params["context_id"] = launch_data.launch_params.context_id
        extra_params["user_id"] = launch_data.launch_params.user_id
        user = User.objects.get(id=launch_data.user.id)
        LTILaunchRecord.objects.create(
            user=user,
            course_key=launch_data.course_key,
            usage_key=launch_data.usage_key,
            context_label=extra_params.pop("context_label", None),
            context_title=extra_params.pop("context_title", None),
            extra_data=extra_params,
        )


LTI_PROVIDER_LAUNCH_SUCCESS.connect(record_lti_provider_launch_success)
