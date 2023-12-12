import asyncio
import pytest

async def some_async_function():
    return 42

async def some_async_function_that_raises():
    raise ValueError("Some error message")

# Использую декораторы pytest.mark.asyncio и pytest.mark.parametrize
@pytest.mark.asyncio
@pytest.mark.parametrize("async_function, expected_value", [
    (some_async_function, 42),
    (some_async_function_that_raises, ValueError("Some error message")),
])
async def test_async_functions(async_function, expected_value):
    try:
        # Вызываю асинхронную функцию и ждем ее выполнения
        result = await async_function()
        # Проверяем результат выполнения
        assert result == expected_value
    except Exception as e:
        # Если при выполнении возникла ошибка
        if isinstance(expected_value, type(e)):
            # Проверяем, что тип ошибки совпадает с ожидаемым
            assert str(e) == str(expected_value)
        else:
            # Если тип ошибки не совпадает с ожидаемым, то выбрасываем исключение
            raise e
