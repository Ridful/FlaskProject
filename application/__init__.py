from flask import Blueprint, Flask, render_template

from .endpoints.views import views_bp
from .endpoints.auth import auth_bp

endpoints: dict[str, Blueprint] = {
    "views": views_bp,
    "auth": auth_bp
}

app = Flask(__name__)

#app.register_blueprint(views_bp, url_prefix='/')
#app.register_blueprint(auth_bp, url_prefix='/')

#register the endpoints to our app instance
for endpoint in endpoints:
    #if callable(endpoints[endpoint]):
    
    #specify url prefix individually in each endpoint.py file
    app.register_blueprint(endpoints[endpoint], url_prefix=endpoints[endpoint].url_prefix)