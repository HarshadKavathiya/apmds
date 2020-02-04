from flask_restful import (Resource, reqparse)

from common.constants import APIMessages
from common.response import (api_response, STATUS_OK)


class EventAPI(Resource):
    def get(self):
        event_api_parser = reqparse.RequestParser()
        event_api_parser.add_argument('event_id',
                                      help="Event ID Required", required=True,
                                      type=int, location='args')

        event_api_parser.add_argument('is_incremental',
                                      help="Event ID Required", required=False,
                                      type=int, location='args')
        event_api_args = event_api_parser.parse_args()

        stubhub_id = event_api_args['event_id']

        data = {"stubhub_id": stubhub_id}

        return api_response(True, APIMessages.SUCCESS,
                            STATUS_OK, data)
