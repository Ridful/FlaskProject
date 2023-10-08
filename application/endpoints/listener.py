from flask import Blueprint, request

listener_bp = Blueprint('listener', __name__, static_folder="static", template_folder="templates", url_prefix="/")

@listener_bp.route("/reg", methods=["POST"])
def registerAgent():
    #username = request.json["name"]
    if request.method == "POST" and request.is_json:
        
        data = request.get_json()
        
        #Register data about new agent to database
        name = data["name"]
        ip = request.remote_addr
        
        #encrypted key to use for comms with endpoints for AAA reasons
        formatted_msg = "api-key"
        
        return (formatted_msg, 200)

    else:
        return ("register failed", 204)
    
#@listener_bp.route("/tasks/<>", methods=["GET"])
#def serveTasks(name):
#    return