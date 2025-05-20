"""
Tests for lti_launch_monitor.signals.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from opaque_keys.edx.keys import CourseKey, UsageKey
from openedx_events.learning.data import LtiProviderLaunchData, LtiProviderLaunchParamsData, UserData, UserPersonalData
from openedx_events.learning.signals import LTI_PROVIDER_LAUNCH_SUCCESS

from lti_launch_monitor.models import LTILaunchRecord
from lti_launch_monitor.signal_handlers import record_lti_provider_launch_success

User = get_user_model()


class TestRecordLTIProviderLaunchSuccess(TestCase):
    """
    Test suite for verifying LTI provider launch record creation.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123",
        )
        user_data = UserData(
            id=self.user.id,
            is_active=True,
            pii=UserPersonalData(
                username="testuser",
                email="testuser@example.com",
                name="Test User",
            ),
        )
        self.course_key = CourseKey.from_string("course-v1:test+course+2024")
        self.usage_key = UsageKey.from_string("block-v1:test+course+2024+type@xblock+block@test-usage")
        self.launch_data = LtiProviderLaunchData(
            user=user_data,
            course_key=self.course_key,
            usage_key=self.usage_key,
            launch_params=LtiProviderLaunchParamsData(
                roles="student",
                context_id="test-context-id",
                user_id="test-user-id",
                extra_params={
                    "context_label": "Test Course Context",
                    "context_title": "Test Course Title",
                    "extra_param1": "Extra Value 1",
                },
            ),
        )

    def test_lti_provider_launch_creates_record(self):
        initial_record_count = LTILaunchRecord.objects.count()
        LTI_PROVIDER_LAUNCH_SUCCESS.send_event(
            launch_data=self.launch_data,
        )
        assert LTILaunchRecord.objects.count() == initial_record_count + 1

        created_record = LTILaunchRecord.objects.last()
        assert created_record.course_key == self.course_key
        assert created_record.usage_key == self.usage_key
        assert created_record.context_label == "Test Course Context"
        assert created_record.context_title == "Test Course Title"
        assert created_record.extra_data == {
            "roles": "student",
            "user_id": "test-user-id",
            "context_id": "test-context-id",
            "extra_param1": "Extra Value 1",
        }
        assert created_record.user == self.user

    def test_lti_provider_launch_with_no_data_does_nothing(self):
        initial_record_count = LTILaunchRecord.objects.count()
        record_lti_provider_launch_success(launch_data=None)
        assert LTILaunchRecord.objects.count() == initial_record_count
