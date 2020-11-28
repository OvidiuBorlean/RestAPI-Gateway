#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import subprocess


app = Flask(__name__)
api = Api(app)

class Hosts(Resource):
   def post(self):
      ReceivedData = request.get_json()
      id = ReceivedData["id"]
      hostname = ReceivedData["hostname"]
      status = ReceivedData["status"]
      int(id)

      #hostName = hostData["hostname"]
      parsedAnswer = "Received " + str(id) + hostname + status
      AnswerData = {
           "Message" : parsedAnswer,
           "StatusCode" : 200
      }
      return jsonify(AnswerData)
#return jsonify(hostData)

def net_module():
   out = subprocess.run("./runModule.sh", shell=True)
   return "Machine Created Successfull"


class Machines(Resource):
    def post(self):

        MachineData = request.get_json()
        machineID = MachineData["id"]
        machineName = MachineData["name"]
        machineAction = MachineData["action"]
        machineStatus = MachineData["status"]
        vmStatus = False
        if machineAction == "create":
           net_module()
           vmStatus = True
        returnData = {
             "StatusCode" : 200,
             "MachineID" : machineID,
             "machineName" : machineName,
             "machineAction" : machineAction,
             "machineStatus" : net_module(),
             "vmStatus": vmStatus
        }
        return jsonify(returnData)


api.add_resource(Hosts, "/hosts")
api.add_resource(Machines, "/machines")



@app.route('/')
def hello_world():
   return("RestAPI Automation Tool")


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
