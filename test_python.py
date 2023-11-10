import asyncio
import pytest

async def some_async_function():
    return 42

async def some_async_function_that_raises():
    raise ValueError("Some error message")

@pytest.mark.asyncio
@pytest.mark.parametrize("async_function, expected_value", [
    (some_async_function, 42),
    (some_async_function_that_raises, ValueError("Some error message")),
])
async def test_async_functions(async_function, expected_value):
    if asyncio.iscoroutinefunction(async_function):
        result = await async_function()
        assert result == expected_value
    else:
        with pytest.raises(expected_value.__class__) as exc_info:
            await async_function()

        assert str(exc_info.value) == str(expected_value)