"""
Database models for lti_launch_monitor.
"""

from django.contrib.auth import get_user_model
from django.db import models
from model_utils.fields import AutoCreatedField
from opaque_keys.edx.django.models import CourseKeyField, UsageKeyField

User = get_user_model()


class LTILaunchRecord(models.Model):
    """
    Model to contain record of all LTI launches.
    """

    created = AutoCreatedField()
    course_key = CourseKeyField(max_length=255)
    usage_key = UsageKeyField(max_length=255)
    context_label = models.CharField(max_length=255)
    context_title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    extra_data = models.JSONField()
