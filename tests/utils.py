import os

import pytest


def requires_api_key(env_var):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not os.environ.get(env_var):
                pytest.skip(
                    f"Environment variable '{env_var}' is not set, skipping the test."
                )
            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator
<<<<<<< HEAD
=======


def skip_in_ci(test_function):
    return pytest.mark.skipif(
        os.environ.get("CI") == "true",
        reason="This test doesn't work on GitHub Actions.",
    )(test_function)
>>>>>>> da48f9c972492f6ed7ae0c05813ee009d9438a7c
