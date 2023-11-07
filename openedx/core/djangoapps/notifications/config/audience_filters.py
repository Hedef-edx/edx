from abc import abstractmethod

from common.djangoapps.course_modes.models import CourseMode
from common.djangoapps.student.models import CourseEnrollment
from openedx.core.djangoapps.course_groups.cohorts import get_cohort_by_name
from openedx.core.djangoapps.django_comment_common.models import Role, FORUM_ROLE_ADMINISTRATOR, FORUM_ROLE_MODERATOR, \
    FORUM_ROLE_GROUP_MODERATOR, FORUM_ROLE_COMMUNITY_TA, FORUM_ROLE_STUDENT


class NotificationAudienceFilterBase:
    """
    Base class for notification audience filters
    """
    def __init__(self, course_key):
        self.course_key = course_key

    allowed_filters = []

    def is_valid_filter(self, values):
        return all(value in self.allowed_filters for value in values)

    @abstractmethod
    def filter(self, values):
        pass


class RoleAudienceFilter(NotificationAudienceFilterBase):
    """
    Filter class for roles
    """
    # TODO: Add course roles to this. We currently support only forum roles
    allowed_filters = [
        FORUM_ROLE_ADMINISTRATOR,
        FORUM_ROLE_MODERATOR,
        FORUM_ROLE_GROUP_MODERATOR,
        FORUM_ROLE_COMMUNITY_TA,
        FORUM_ROLE_STUDENT,
    ]

    def filter(self, roles):
        """
        Filter users based on their roles
        """
        if not self.is_valid_filter(roles):
            return None
        return Role.course_users_with_role(self.course_key, roles)


class EnrollmentAudienceFilter(NotificationAudienceFilterBase):
    """
    Filter class for enrollment modes
    """
    allowed_filters = CourseMode.ALL_MODES

    def filter(self, enrollment_modes):
        """
        Filter users based on their course enrollment modes
        """
        if not self.is_valid_filter(enrollment_modes):
            return None
        return CourseEnrollment.objects.filter(
            course_id=self.course_key,
            mode__in=enrollment_modes,
        ).values_list('user_id', flat=True)


class CohortAudienceFilter(NotificationAudienceFilterBase):
    """
    Filter class for cohorts
    """

    def filter(self, cohort_name):
        """
        Filter users based on cohort name provided
        """
        cohort_user_ids = get_cohort_by_name(self.course_key, cohort_name).values_list('users__id', flat=True)
        if not cohort_user_ids:
            return None
        return cohort_user_ids
