from safrs import SAFRSAPI
import safrs
from database import models
import logging as logging

app_logger = logging.getLogger('api_logic_server_app')
app_logger.info("api/expose_api_models.py - endpoint for each table")


def expose_models(app, HOST="localhost", PORT=5656, API_PREFIX="/api"):
    """ create SAFRSAPI, exposing each model (note: end point names are table names) """
    app_logger.debug(f"api/expose_api_models -- host = {HOST}, port = {PORT}")
    api = SAFRSAPI(app, host=HOST, port=PORT, prefix = API_PREFIX)
    safrs_log_level = safrs.log.getEffectiveLevel()
    if True or app_logger.getEffectiveLevel() >= logging.INFO:
        safrs.log.setLevel(logging.WARN)  # warn is 20, info 30
    api.expose_object(models.Category)
    api.expose_object(models.Customer)
    api.expose_object(models.CustomerDemographic)
    api.expose_object(models.Department)
    api.expose_object(models.Employee)
    api.expose_object(models.EmployeeAudit)
    api.expose_object(models.EmployeeTerritory)
    api.expose_object(models.Territory)
    api.expose_object(models.Location)
    api.expose_object(models.Order)
    api.expose_object(models.OrderDetail)
    api.expose_object(models.Product)
    api.expose_object(models.Region)
    api.expose_object(models.Shipper)
    api.expose_object(models.Supplier)
    safrs.log.setLevel(safrs_log_level)
    return api
