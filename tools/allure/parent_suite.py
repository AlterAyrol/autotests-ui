from enum import Enum


class AllureParentSuite(str, Enum):
    LMS = "LMS system"
    STUDENT = "Student system"
    ADMINISTRATION = "Administration system"
