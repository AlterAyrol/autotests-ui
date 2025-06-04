from enum import Enum


class AllureSubSuite(str, Enum):
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"
