from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication


class JwtTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f'Path: {request.path}, Method: {request.method}')
        if (request.path.startswith('/api/jwt/')
                or (request.path.startswith('/api/user') and request.method == 'POST')
                or request.path.startswith('/admin')
                or request.path.startswith('/api/schema')
                or request.path.startswith('/api/docs')):
            return self.get_response(request)

        jwt_authenticator = JWTAuthentication()
        # authenticate() verifies and decode the token
        # if token is invalid, it raises an exception and returns 401
        response = jwt_authenticator.authenticate(request)
        if response is not None:
            # unpacking
            user, token = response
            print("this is decoded token claims", token.payload)
            request.user_id = token.payload.get('user_id')
            response = self.get_response(request)
            return response
        else:
            error = {'message': 'invalid token'}
            print("no token is provided in the header or the header is missing")
            return JsonResponse(error, status=401)
