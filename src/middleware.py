import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class TimeoutMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        start = time.time()
        print(f"[Middleware] Incoming request: {request.method} {request.url.path}")

        response = await call_next(request)

        duration = time.time() - start
        print(f"[Middleware] Request {request.url.path} took {duration:.2f}s")
        response.headers["X-Process-Time"] = str(round(duration, 4))

        return response
