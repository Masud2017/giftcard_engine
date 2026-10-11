from starlette.middleware.base import BaseHTTPMiddleware

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        
        firebase_auth_token = request.headers.get("bearer")
        
        return response