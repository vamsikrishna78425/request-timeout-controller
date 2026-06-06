import asyncio
from fastapi import FastAPI
from src.timeout_manager import TimeoutManager
from src.middleware import TimeoutMiddleware

app = FastAPI(
    title="Request Timeout Controller",
    description="Reliability Module - Prevents indefinitely running requests",
    version="1.0.0"
)

app.add_middleware(TimeoutMiddleware)
manager = TimeoutManager()

async def process_request(delay: float):
    await asyncio.sleep(delay)
    return "completed"

async def multi_step_task(delay: float):
    print("[Task] Step 1: Database Update... Done")
    await asyncio.sleep(1)
    print("[Task] Step 2: Cache Update... Done")
    await asyncio.sleep(1)
    print("[Task] Step 3: Notification Delivery... Running")
    await asyncio.sleep(delay)
    return "all steps completed"

@app.get("/")
async def root():
    return {"message": "Request Timeout Controller is running"}

@app.get("/request/{request_id}")
async def handle_request(request_id: str, delay: float = 2.0, timeout: float = 5.0):
    result = await manager.execute(
        request_id=request_id,
        coro=process_request(delay),
        timeout=timeout
    )
    return result

@app.get("/multistep/{request_id}")
async def handle_multistep(request_id: str, delay: float = 5.0, timeout: float = 4.0):
    result = await manager.execute(
        request_id=request_id,
        coro=multi_step_task(delay),
        timeout=timeout
    )
    return result
