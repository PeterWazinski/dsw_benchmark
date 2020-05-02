import connexion
import os
from typing import Dict

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

def get_predictinterface() -> Dict:
    print("Dict")
    return {"devicetypes": ["5W8C1H", "5W8C50"],  # some promag 800 dev types
            "specs": ["eh.flow.mid.fastmeasures.mid_mediumtemperature", "eh.flow.cdm.fastmeasurements.flow_out1value"]}


def post_predict(input: Dict) -> Dict:
    """
       return  of "eh.flow.mid.fastmeasures.mid_mediumtemperature"  + "eh.flow.cdm.fastmeasurements.flow_out1value"
    """

    v1 = input.get("eh.flow.mid.fastmeasures.mid_mediumtemperature")
    v2 = input.get("eh.flow.cdm.fastmeasurements.flow_out1value")

    return {"predict_type": "some regression",
            "prediction": float(v1) + float(v2)}


def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'secret':
        return {'sub': 'admin'}
    else:
        # optional: raise exception for custom error response
        return None


if __name__ == '__main__':
    print("\n open swagger ui with http://localhost:9090/v1.0/ui\n credentials= admin/secret \n")
    app = connexion.FlaskApp(__name__, port=9090, host=hostname, specification_dir='.')

    #openapi 3.0 yaml
    #app.add_api('dsw_netilion_client-api.yaml', arguments={'title': 'DSW Netilion Client'})

    # swagger 2.0 yaml
    app.add_api('dsw_netilion_swagger.yaml', arguments={'title': 'DSW Netilion Client'})
    app.run()

