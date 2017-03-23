# Prism framework

Prism developer-focused API-first Python framework. Our priority is to make your life easier when working with Python.

## Getting started

```python
from prism import server, router

def hello(request):
  return 'hello world'

router.get('/hello', hello)

server.run()
```
