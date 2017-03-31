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

Or if you use the example boilerplate 

```bash
python3 -m prism.example.wizard run
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

You can of course use a function and multiple params (you can still use a lambda but it's not readable anymore).

```python
def handler(request, name, age):
    return 'Hello, you are {} and you are {} years old'.format(name, age)

router.get('/hello/<name>/age/<age>', handler) 
```

### Middlewares

You can define middlewares for your routes using the `via` method. A middleware takes the request as its only argument.
Your function can return `False` to block the request, this can be useful for authentication and right checking. 

```python
def guest(request):
  return request.is_guest()

router.get('/some/guest/page', some_guest_view).via(guest)
```

You can also pass a list of methods to `via`

```python
router.get('/some/guest/page', some_guest_view).via([a, b, c])
```


## Requests

Prism provides a nice wrapper around the request. As we said before, a Request instance is passed to every route handler as its first parameter.

### Request input

You can get all user input (url and body) in one method, no matter the content type etc..

```python
input = request.all() # {'param': value}
```

You can also get a specific key

```python
input = request.input('key', None) # Returns the value for 'key' or None
```

Following the same logic, you also have a file method to get the files sent as POST parameters.

```python
input = request.file('filename') # Returns the file or None
```

If you specifically want the URL params or the POST/PUT body, you can use the following properties 

```python
url_params = request._params

body = request._data
```

### Request headers

You can get all headers as a `dict` using the `headers` property.

```python
input = request.headers # {'Content-Type': 'text/html'}
```

Or get a specific one

```python
input = request.header('User-Agent') # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) [...]'
```

### Request infos

**Path**

```python
request.path # '/path/of/the/request'
```

**Method**

```python
request.method # 'GET'
```

**Host**

```python
request.host # 'localhost:5555'
```

**Host URL**

```python
request.host_url # 'http://localhost:5555'
```







