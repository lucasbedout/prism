from prism.kernel import application
from werkzeug.serving import run_simple

class Server:

  def run(self, host='0.0.0.0', port=5555):
      run_simple(host, port, application, threaded=True)

server = Server()

