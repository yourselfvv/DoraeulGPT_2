import time

from openai import util
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource
from openai.error import TryAgain


class Completion(EngineAPIResource):
    OBJECT_NAME = "completions"

    @classmethod
    def create(cls, *args, **kwargs):
        start = time.time()
        timeout = kwargs.pop("timeout", None)

        while True:
            try:
                return super().create(*args, **kwargs)
            except TryAgain as e:
                if timeout is not None and time.time() > start + timeout:
                    raise

                util.log_info("Waiting for model to warm up", error=e)

    @classmethod
    async def acreate(cls, *args, **kwargs):
        start = time.time()
        timeout = kwargs.pop("timeout", None)

        while True:
            try:
                return await super().acreate(*args, **kwargs)
            except TryAgain as e:
                if timeout is not None and time.time() > start + timeout:
                    raise

                util.log_info("Waiting for model to warm up", error=e)
