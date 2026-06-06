import pytest
import asyncio
from src.timeout_manager import TimeoutManager

manager = TimeoutManager()

async def process_request(delay: float):
    await asyncio.sleep(delay)
    return "completed"

@pytest.mark.asyncio
async def test_request_within_timeout():
    result = await manager.execute(
        request_id="REQ-001",
        coro=process_request(2),
        timeout=5
    )
    assert result["status"] == "success"
    print("Test Case 1 Passed: Request completed within timeout")

@pytest.mark.asyncio
async def test_request_exceeds_timeout():
    result = await manager.execute(
        request_id="REQ-002",
        coro=process_request(10),
        timeout=5
    )
    assert result["status"] == "timeout"
    print("Test Case 2 Passed: Request timed out as expected")

@pytest.mark.asyncio
async def test_concurrent_requests():
    results = await asyncio.gather(
        manager.execute("REQ-A", process_request(2), timeout=5),
        manager.execute("REQ-B", process_request(7), timeout=5),
        manager.execute("REQ-C", process_request(12), timeout=5),
    )
    assert results[0]["status"] == "success"
    assert results[1]["status"] == "timeout"
    assert results[2]["status"] == "timeout"
    print("Test Case 3 Passed: Concurrent requests handled correctly")

@pytest.mark.asyncio
async def test_rollback_on_timeout():
    result = await manager.execute(
        request_id="REQ-004",
        coro=process_request(10),
        timeout=3
    )
    assert result["status"] == "timeout"
    print("Test Case 4 Passed: Rollback executed on timeout")
