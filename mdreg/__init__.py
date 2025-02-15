import base64
import requests
url = 'https://api.github.com/repos/QIB-Sheffield/mdreg/contents/README.md'
req = requests.get(url)
if req.status_code == requests.codes.ok:
    req = req.json()  # the response is a JSON
    content = base64.b64decode(req['content'])
    introduction = content.decode()
__doc__ = introduction

from .main import *
__all__ = ['MDReg', 'models']