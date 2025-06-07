from enum import Enum

class AppRoute(str, Enum):
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"
    DASHBOARD = "./#/dashboard"
    MAIN_COURSE = "./#/courses"
    CREATE_COURSE = "./#/courses/create"