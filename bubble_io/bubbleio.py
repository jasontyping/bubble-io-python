import requests
from bubble_io.auth import BubbleIoAuth


class BubbleIoException(Exception):
    pass


class BubbleIo:
    BUBBLE_API_DOMAIN = "bubbleapps.io"
    BUBBLE_API_PATH = "api/"

    def __init__(self, app_name, domain_name=None, secure=True, live=False, api_token=None, api_version_string="1.1"):
        session = requests.Session()
        session.auth = BubbleIoAuth(api_token)

        self._session = session
        self._api_url = ("https" if secure else "http") + \
            "://" + ((app_name + "." + self.BUBBLE_API_DOMAIN)
                     if not domain_name else domain_name) + ("/version-test" if not live else "") + "/" + self.BUBBLE_API_PATH + api_version_string + "/"

    def _get(self, api_path):
        r = self._session.get(self._api_url+api_path)

        return r.json()

    def get_things_all(self, type_name):
        # For API calls, thing names are always lower case with no spaces, regardless of
        # How they are named in the UI
        sanitized_type_name = type_name.lower().replace(" ", "")
        all_things = []

        things = self._get("obj/" + sanitized_type_name + "/")

        if("response" in things and "results" in things["response"]):
            all_things += things["response"]["results"]
        else:
            raise BubbleIoException(things["error_class"])

        return(all_things)
