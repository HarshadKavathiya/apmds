import os

from flask import send_from_directory

from api.event import EventAPI
from common.common_exception import (UnauthorizedException,
                                     ResourceNotAvailableException,
                                     GenericBadRequestException,
                                     IllegalArgumentException)
from common.constants import APIMessages
from common.response import (api_response, STATUS_FORBIDDEN,
                             STATUS_BAD_REQUEST)
from index import (app, api, static_folder)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """
    Serve HTML/React Static content i.e. HTML, CSS, JS, image, font files.

    Args:
        path(str): path for folder or resource in case of backend api

    Returns: return HTML/React Static content i.e. HTML, CSS, JS file

    """
    if path != "" and os.path.exists(static_folder + path):
        return send_from_directory(static_folder, path)
    elif not (os.path.exists(static_folder + path) or (
            str(path).startswith("api/"))):
        return send_from_directory(static_folder, 'index.html')
    elif path == "":
        return send_from_directory(static_folder, 'index.html')


# @app.errorhandler(Exception)
# def handle_exception(e):
#     """Handle Generic Exception."""
#     return api_response(False, APIMessages.INTERNAL_ERROR, STATUS_SERVER_ERROR,
#                         {'error_log': str(e)})


@app.errorhandler(UnauthorizedException)
def handle_unauthorized_exception(e):
    """Handle Unauthorized Access Exception."""
    return api_response(False, APIMessages.FORBIDDEN, STATUS_FORBIDDEN)


@app.errorhandler(ResourceNotAvailableException)
def handle_resource_not_available_exception(e):
    """Handle Resource Not Available Exception."""
    return api_response(
        False, APIMessages.NO_RESOURCE.format(e), STATUS_BAD_REQUEST)


@app.errorhandler(GenericBadRequestException)
def handle_bad_request_exception(e):
    """Handle Generic Bad Request Exception."""
    return api_response(False, str(e), STATUS_BAD_REQUEST)


@app.errorhandler(IllegalArgumentException)
def handle_bad_request_exception(e):
    """Handle  Illegal Argument Exception."""
    return api_response(False, str(e), STATUS_BAD_REQUEST)


@app.errorhandler(IllegalArgumentException)
def handle_bad_request_exception(e):
    """Handle  Illegal Argument Exception."""
    return api_response(False, str(e), STATUS_BAD_REQUEST)


api.add_resource(EventAPI, "/api/event", "/")
# api.add_resource(EventAPI, "/")
