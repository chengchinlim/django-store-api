import json

from django.http import JsonResponse


class JsonResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if isinstance(response, JsonResponse):
            data = response.content
            # from byte to json object
            str_data = data.decode('utf-8')
            json_obj = json.loads(str_data)

            formatted_data = {
                'status': response.status_code
            }
            if json_obj.get('item') is not None:
                formatted_data['item'] = json_obj['item']
            if json_obj.get('items') is not None:
                formatted_data['items'] = json_obj['items']
            if json_obj.get('extra') is not None:
                formatted_data['extra'] = json_obj['extra']

            # from json object to byte
            result_str_data = json.dumps(formatted_data)
            byte_data = result_str_data.encode('utf-8')
            response.content = byte_data

        return response
