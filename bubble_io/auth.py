import os
import requests


class BubbleIoAuth(requests.auth.AuthBase):
    def __init__(self, api_token=None):
        try:
            self._api_token = api_token or os.environ["BUBBLEIO_API_TOKEN"]
        except KeyError:
            raise KeyError(
                "Bubble.io API Token not found. api_token must be provided to BubbleIoAuth \
                            or set in the environment variable BUBBLEIO_API_TOKEN"
            )

    def __call__(self, request):
        auth_token = {"Authorization": "Bearer {}".format(self._api_token)}
        request.headers.update(auth_token)
        return request
