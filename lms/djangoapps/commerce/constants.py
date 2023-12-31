""" Constants for this app as well as the external API. """


# .. toggle_name: transition_to_coordinator.order_create
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: Allows to post order to Commerce Coordinator API
# .. toggle_use_cases: open_edx
# .. toggle_creation_date: 2023-07-18
# .. toggle_tickets: THES-68
# .. toggle_status: supported
ENABLE_COORDINATOR_ORDER_CREATE = 'transition_to_coordinator.order_create'
COORDINATOR_ORDER_CREATE_PATH = '/lms/order'


class OrderStatus:
    """Constants representing all known order statuses. """
    OPEN = 'Open'
    FULFILLMENT_ERROR = 'Fulfillment Error'
    COMPLETE = 'Complete'


class Messages:
    """ Strings used to populate response messages. """
    NO_ECOM_API = 'E-Commerce API not setup. Enrolled {username} in {course_id} directly.'
    NO_SKU_ENROLLED = 'The {enrollment_mode} mode for {course_id}, {course_name}, does not have a SKU. Enrolling ' \
                      '{username} directly. Course announcement is {announcement}.'
    ENROLL_DIRECTLY = 'Enroll {username} in {course_id} directly because no need for E-Commerce baskets and orders.'
    ORDER_COMPLETED = 'Order {order_number} was completed.'
    ORDER_INCOMPLETE_ENROLLED = 'Order {order_number} was created, but is not yet complete. User was enrolled.'
    NO_HONOR_MODE = 'Course {course_id} does not have an honor mode.'
    NO_DEFAULT_ENROLLMENT_MODE = 'Course {course_id} does not have an honor or audit mode.'
    ENROLLMENT_EXISTS = 'User {username} is already enrolled in {course_id}.'
    ENROLLMENT_CLOSED = 'Enrollment is closed for {course_id}.'
