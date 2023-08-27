import json
import time

from django.http import JsonResponse
from store_rest_api.util import is_json_array


class JsonResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_hash = time.time_ns()
        # print before start the request (debug)
        print(request_hash, request.body.decode('utf-8'))
        request.hash = request_hash

        response = self.get_response(request)

        if isinstance(response, JsonResponse):
            data = response.content
            # from byte to json object
            str_data = data.decode('utf-8')
            json_obj = json.loads(str_data)

            formatted_data = {
                'status': response.status_code
            }
            data = json_obj.get('data')
            if json_obj.get('data') is not None:
                if is_json_array(data):
                    formatted_data['items'] = data
                else:
                    formatted_data['item'] = data
            elif json_obj.get('items') is not None:
                formatted_data['items'] = json_obj['items']

            if json_obj.get('extra') is not None:
                formatted_data['extra'] = json_obj['extra']
            if json_obj.get('errors') is not None:
                formatted_data['errors'] = json_obj['errors']

            # assume all above fields are empty
            if len(formatted_data) <= 1:
                formatted_data['unexpected'] = json_obj

            # from json object to byte
            result_str_data = json.dumps(formatted_data)
            byte_data = result_str_data.encode('utf-8')
            response.content = byte_data

        return response
