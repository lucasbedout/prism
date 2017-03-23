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

## Routing

### Basics

Prism `router` offers you many helpers to make routing a breeze. To use it, you need to include the singleton.

```python
from prism import router
```

Here is the most basic example, using a lambda.

```python
router.get('/', lambda request: 'Welcome!')
```

You can use any function as the second parameter. The router will always pass the request as the first parameter.

```python
from views import method

router.get('/', method)
```

### Available methods

The router exposes obvious methods for the main HTTP methods.

```python
router.post('/form', lambda request: 'This is a POST')

router.put('/form', lambda request: 'This is a PUT')

router.delete('/form', lambda request: 'This is a DELETE')
```

### Route parameters

You can pass route parameters using the `<>` syntax. 

```python
router.get('/hello/<name>', lambda request, name: 'Hello ' + name) 
```

You can of course use a function and multiple params (you can still use a lambda but it's not readable anymore.

```python
def handler(request, name, age):
    return 'Hello, you are {} and you are {} years old'.format(name, age)

router.get('/hello/<name>/age/<age>', handler) 
```








