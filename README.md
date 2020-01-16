# requests-llnw-auth
This module provides an authentication plugin for Requests to generate the X-LLNW-Security-* request headers required by Limelight Networks APIs.

## Getting Started
Firstly, install the package:
```
pip install requests-llnw-auth
```

Then in your Python script, create an `LLNWAuth` object, using your Limelight Control username and API key, and pass it to a `requests` function using the `auth` keyword attribute.
```python
import requests
from requests_llnw_auth import LLNWAuth

llnw_auth = LLNWAuth('username', 'api_key')
shortname = 'yourshortname'
res = requests.get(f'https://apis.llnw.com/config-api/v1/svcinst/delivery/shortname/{shortname}', auth=llnw_auth)
```
