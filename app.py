# app.py

from werkzeug.middleware.dispatcher import DispatcherMiddleware # use to combine each Flask app into a larger one that is dispatched based on prefix
from api_logic_server_run import flask_app as api_app_1
from admin_api import create_app as create_admin_app, User, Api
from safrs import SAFRSAPI as SafrsApi


def create_api(app, host="localhost", port=5000, api_prefix="/api", app_prefix="/admin", models = []):
    """
        create the swagger blueprint
        create the api endpoints
    """
    from flask_swagger_ui import get_swaggerui_blueprint
    
    api_spec_url = f"/swagger"
    swaggerui_blueprint = get_swaggerui_blueprint(
        api_prefix, f"{app_prefix}{api_prefix}{api_spec_url}.json", config={"docExpansion": "none", "defaultModelsExpandDepth": -1}
    )
    
    app.register_blueprint(swaggerui_blueprint, url_prefix=api_prefix)
    api = SafrsApi(app, 
                    host=host,
                    port=port,
                    prefix=api_prefix,
                    swaggerui_blueprint=swaggerui_blueprint,
                    api_spec_url=api_spec_url,
                    custom_swagger={"basePath" : f"{app_prefix}{api_prefix}"} )

    for model in models:
        api.expose_object(model)
    api.expose_als_schema(api_root=f"//{host}:{port}{app_prefix}{api_prefix}")
    print(f"Created API: http://{host}:{port}{app_prefix}{api_prefix}")


host = "localhost"
port = 5656
admin_app = create_admin_app(host=host)
with admin_app.app_context():
    create_api(admin_app, host=host, port=port, api_prefix="/api", app_prefix="/admin", models = [User,Api])


application = DispatcherMiddleware(api_app_1, {
    '/admin': admin_app
})
