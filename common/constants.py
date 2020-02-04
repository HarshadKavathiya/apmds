"""File to store all constants."""


class APIMessages:
    """Messages to be sent in API Responses."""

    SUCCESS = "Success"
    NO_RESOURCE = "{} is not available"
    INTERNAL_ERROR = "Internal Server Error"
    FORBIDDEN = "Access Denied"


class GenericStrings:
    """Class to store generic strings that are referenced in code."""

    EMAIL_FORMAT_REGEX = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class TimeOuts:
    """Timeouts to be referenced in the code."""

    TEN_DAYS_IN_HOURS = 240
    HUNDRED_DAYS = 100
    ONE_DAY_IN_SECONDS = 60 * 60 * 24
