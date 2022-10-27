import logging

import azure.functions as func
import json
from datetime import date, timedelta


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Calculate days until next wednesday"""
    logging.info('Python HTTP trigger function processed a request.')
    
    today = date.today()
    wednesday = today + timedelta((2 - today.weekday()) % 7)
    
    # return shield.io json
    return func.HttpResponse(json.dumps({
        "schemaVersion": 1,
        "label": "days until wednesday",
        "message": str((wednesday - today).days),
        "color": "blue",
    }))
    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    # )
