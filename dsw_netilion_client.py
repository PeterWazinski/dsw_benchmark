import connexion
import os


def is_docker():
    """is python running inside a docker image?"""
    path = '/proc/self/cgroup'
    return (
            os.path.exists('/.dockerenv') or
            os.path.isfile(path) and any('docker' in line for line in open(path))
    )


hostname = "127.0.0.1"  # localhost
if is_docker():
    hostname = "0.0.0.0"  # allow port remapping when running docker image

from typing import Dict


def post_predictinterface() -> Dict:
    print("Dict")
    return {"devicetypes": ["5W8C1H", "5W8C50"],  # some promag 800 dev types
            "specs": ["eh.flow.mid.fastmeasures.mid_mediumtemperature"]}


def post_predict(input: Dict) -> Dict:
    """
    Assume linear regression: f(x) = 2x+1
    input = {'value':123}
    """
    val = int(input.get("value"))
    return {"predict_type": "some regression",
            "prediction": 2 * val + 1}


def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'secret':
        return {'sub': 'admin'}
    else:
        # optional: raise exception for custom error response
        return None


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, host=hostname, specification_dir='.')
    app.add_api('dsw_netilion_client-api.yaml', arguments={'title': 'DSW Netilion Client'})
    app.run()
