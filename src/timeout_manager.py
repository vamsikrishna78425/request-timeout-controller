import asyncio

class TimeoutManager:

    async def execute(self, request_id: str, coro, timeout: float):
        print(f"[TimeoutManager] Starting request: {request_id}")

        try:
            result = await asyncio.wait_for(
                coro,
                timeout=timeout
            )
            print(f"[TimeoutManager] Request {request_id} completed successfully.")
            return {
                "status": "success",
                "request_id": request_id,
                "result": result
            }

        except asyncio.TimeoutError:
            print(f"[TimeoutManager] Request {request_id} timed out after {timeout}s.")
            await self.rollback(request_id)
            return {
                "status": "timeout",
                "request_id": request_id,
                "message": f"Request cancelled due to timeout after {timeout} seconds"
            }

    async def rollback(self, request_id: str):
        print(f"[Rollback] Reverting completed operations for request: {request_id}")
