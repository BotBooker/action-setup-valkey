import os
import typing as t
import pytest
import redis

ConnectionFactory = t.Callable[[str], redis.Redis]


@pytest.fixture(scope="function")
def connection_uri() -> str:
    """Read and return Valkey connection URI from environment."""
    connection_uri = os.getenv("CONNECTION_URI")
    if connection_uri is None:
        pytest.fail("CONNECTION_URI: environment variable is not set")
    return connection_uri


@pytest.fixture(scope="function")
def connection_factory() -> ConnectionFactory:
    """Return a Valkey client factory from a URI string."""
    def factory(uri: str) -> redis.Redis:
        return redis.Redis.from_url(uri, decode_responses=True)
    return factory


@pytest.fixture(scope="function", params=["uri"])
def valkey_client(
    request: pytest.FixtureRequest,
    connection_factory: ConnectionFactory,
    connection_uri: str,
) -> t.Generator[redis.Redis, None, None]:
    """Return a Valkey client for connection URI set in environment."""
    if request.param == "uri":
        client = connection_factory(connection_uri)
    else:
        raise RuntimeError(f"{request.param}: unknown connection method")

    try:
        client.ping()
    except redis.ConnectionError as e:
        pytest.fail(f"Failed to connect to Valkey via URI: {e}")

    yield client

    try:
        client.flushdb()
    except redis.ConnectionError:
        pass
    finally:
        client.close()


def test_valkey_basic_operations(valkey_client: redis.Redis):
    """Test basic SET, GET and TTL operations in Valkey."""
    assert valkey_client.set("test_key", "hello_valkey") is True
    assert valkey_client.get("test_key") == "hello_valkey"

    valkey_client.rpush("test_list", "item1", "item2")
    assert valkey_client.llen("test_list") == 2
    assert valkey_client.lpop("test_list") == "item1"

    valkey_client.delete("test_key")
    assert valkey_client.get("test_key") is None
