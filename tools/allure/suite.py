from enum import Enum


class AllureSuite(str, Enum):
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    AUTHENTICATION = "Authentication"
