# bubble-io-python
This library provides Python objects that interface with the client API available on the wonderful "no-code" platform [Bubble.io](https://Bubble.io).

Expect this library to be incomplete and not suitable for production use. I wrote this because I needed Python to talk with Bubble for some small projects. I didn't find existing libraries. 

It's not comprehensive. I add functions/objects as I need them. I have limited Python skills, so I'm happy to receive all manner of pull requests.

## Usage examples
### Getting data from a dev instance via the default URL with API token provided as a variable
```python
from bubble_io.bubbleio import BubbleIo

# If api_token is provided it will use that for authentication, otherwise it will use the environment variable 
# named "BUBBLEIO_API_TOKEN"
bubbleio = BubbleIo("my-app-name", api_token="01234567890123456789012345678901")

print(bubbleio.get_things_all("Furniture Inventory"))
```

### Getting data from a live instance via a custom URL and API token in an environment variable

```python
from bubble_io.bubbleio import BubbleIo

# api_token is set in the environment variable named "BUBBLEIO_API_TOKEN"
# A custom domain name "mygreatapp.com" has been set up for the app on Bubble
bubbleio = BubbleIo("my-app-name", domain_name="mygreatapp.com", live=True)

print(bubbleio.get_things_all("Furniture Inventory"))
```