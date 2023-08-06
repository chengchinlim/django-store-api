import json

from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication


class JwtTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwt_authenticator = JWTAuthentication()
        # authenticate() verifies and decode the token
        # if token is invalid, it raises an exception and returns 401
        response = jwt_authenticator.authenticate(request)
        if response is not None:
            # unpacking
            user, token = response
            print("this is decoded token claims", token.payload)
            response = self.get_response(request)
            return response
        else:
            error = {'message': 'invalid token'}
            print("no token is provided in the header or the header is missing")
            return JsonResponse(error, status=401)


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
