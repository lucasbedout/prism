from prism import server, router

def hello(request, name):
  import ipdb; ipdb.set_trace()
  return 'Hello ' + name

router.get('/', lambda request: 'Welcome!')
router.get('/hello/<name>', hello)

server.run()
