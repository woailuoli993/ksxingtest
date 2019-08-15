# `app_context` is the flag to describe where the app is running.
# Cases: Shell/Server/Unittest

app_context = None

APP_CONTEXT_SERVER = 1
APP_CONTEXT_UNITTEST = 2
APP_CONTEXT_SHELL = 3
APP_CONTEXT_SCRIPT = 4


def set_app_context_server():
    global app_context
    if app_context is None:
        app_context = APP_CONTEXT_SERVER


def set_app_context_shell():
    global app_context
    if app_context is None:
        app_context = APP_CONTEXT_SHELL


def set_app_context_unittest():
    global app_context
    if app_context is None:
        app_context = APP_CONTEXT_UNITTEST


def set_app_context_script():
    global app_context
    if app_context is None:
        app_context = APP_CONTEXT_SCRIPT


def is_in_server():
    return app_context == APP_CONTEXT_SERVER


def is_in_shell():
    return app_context == APP_CONTEXT_SHELL


def is_in_unittest():
    return app_context == APP_CONTEXT_UNITTEST


def is_in_script():
    return app_context == APP_CONTEXT_SCRIPT