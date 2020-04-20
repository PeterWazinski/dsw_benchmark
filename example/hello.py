


import connexion
import os


def is_docker():
    path = '/proc/self/cgroup'
    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
    )

hostname = "127.0.0.1"
if is_docker():
    hostname="0.0.0.0"

def post_greeting(name: str) -> str:
    print ("name : " + name)
    return 'Hello {name}'.format(name=name)

def get_greeting2(name: str) -> str:
    print ("name2 : " + name )
    return 'Hello 2x{name}'.format(name=name)


def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'secret':
        return {'sub': 'admin'}
    else:
        # optional: raise exception for custom error response
        return None

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, host=hostname, specification_dir='..')
    app.add_api('helloworld-api.yaml', arguments={'title': 'Hello World Example'})
    app.run()