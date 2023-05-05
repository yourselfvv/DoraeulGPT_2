import os
import sys
from typing import TYPE_CHECKING, Optional, Union, Callable

from contextvars import ContextVar

import openai
if "pkg_resources" not in sys.modules:
    sys.modules["pkg_resources"] = object()


    del sys.modules["pkg_resources"]

from openai.api_resources import (
    Completion,
    Customer,
    Deployment,
    Edit,
    Embedding,
    Engine,
    ErrorObject,
    File,
    FineTune,
    Image,
    Model,
    Moderation,
)
from openai import api_resources
from Data.error import APIError, InvalidRequestError, OpenAIError

if TYPE_CHECKING:
    import requests
    from aiohttp import ClientSession

openai.api_key = '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'
api_key_path: Optional[str] = os.environ.get("OPENAI_API_KEY_PATH")

organization = os.environ.get("OPENAI_ORGANIZATION")
api_base = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
api_type = os.environ.get("OPENAI_API_TYPE", "open_ai")
api_version = (
    "2023-03-15-preview" if api_type in ("azure", "azure_ad", "azuread") else None
)
verify_ssl_certs = True
proxy = None
app_info = None
enable_telemetry = False
ca_bundle_path = None
debug = False
log = None

requestssession: Optional[
    Union["requests.Session", Callable[[], "requests.Session"]]
] = None

aiosession: ContextVar[Optional["ClientSession"]] = ContextVar(
    "aiohttp-session", default=None
)

__all__ = [
    "APIError",
    "Completion",
    "Customer",
    "Edit",
    "Image",
    "Deployment",
    "Embedding",
    "Engine",
    "ErrorObject",
    "File",
    "FineTune",
    "InvalidRequestError",
    "Model",
    "Moderation",
    "OpenAIError",
    "api_base",
    "api_key",
    "api_type",
    "api_key_path",
    "api_version",
    "app_info",
    "ca_bundle_path",
    "debug",
    "enable_telemetry",
    "log",
    "organization",
    "proxy",
    "verify_ssl_certs",
]
def generate_text(prompt):
    import Data
    completions = Data.api_resources.completion.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message