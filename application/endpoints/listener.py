from flask import Blueprint, request
from ..utils.agent import Agent, Results


listener_bp = Blueprint('listener', __name__, static_folder="static", template_folder="templates", url_prefix="/")


@listener_bp.route("/reg", methods=["POST"])
def registerAgent():
    #username = request.json["name"]
    if request.method == "POST" and request.is_json:
        data = request.get_json()
        
        name = data["name"]
        remote_agent_ip = request.remote_addr
        
        new_agent = Agent(name, remote_agent_ip)
        print(f"New Agent: Name:{new_agent.name} | IP:{new_agent.ip} | Joined:{new_agent.joindate} | UUID:{new_agent.uuid}")
        
        #ip = request.remote_addr
        #encrypted key to use for comms with endpoints for AAA reasons
        formatted_msg = new_agent.uuid #"api-key"
        return (formatted_msg, 200)
    
    else:
        return ("register failed", 204)
    
    
@listener_bp.route("/results", methods=["POST"])
def agentActionResults():
    if request.method == "POST" and request.is_json:
        
        data = request.is_json()
        
        agentPostResults = Results
        #agentPostResults.
        
        print(data)
        
        #uuid  ip  past_task  task_result
        #print(f"Results:{new_agent.name} | IP:{new_agent.ip} | Joined:{new_agent.joindate} | UUID:{new_agent.uuid}")
        print(f"{agentPostResults}")
        
        return "oh pass pass"
    else:
        return ("failed to return the results", 404)
    

@listener_bp.route("/tasks/<uuid>", methods=["GET"])
def serveTasks(uuid):
    
    return f"Hello UUID:{uuid}!"


@listener_bp.route("/download/<filename>", methods=["GET"])
def serveDownload(filename):
    
    return f"This is the location of the file: {filename}!"