from flask import Flask
import os
import socket
import json
from watson_developer_cloud import VisualRecognitionV3

# Connect to Redis
app = Flask(__name__)
cred = json.loads(open(os.getenv("svcbindingmountpath")+"/binding","r").read())

@app.route("/")
def hello():
    img_url="http://www.dogbreedslist.info/uploads/allimg/dog-pictures/Rottweiler-1.jpg"
    visual_rec_svc = VisualRecognitionV3(version="2016-05-20",api_key=cred['api_key'])
    clazes = visual_rec_svc.classify(url=img_url,parameters=json.dumps({
            'classifier_ids': ['fruits_1462128776','SatelliteModel_6242312846','default'],
            'threshold': 0.6
        }))

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>VR Credentials: {creden}</b><br/>" \
           "<h2> <a href='{img_url}'> this is the img </a> </h2>" \
           "{filecontent}"
    
    return html.format(name=os.getenv("NAME", "there"), img_url=img_url, hostname=socket.gethostname(),filecontent=json.dumps(clazes),creden=json.dumps(cred))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)
