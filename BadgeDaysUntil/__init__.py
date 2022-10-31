import json
import logging

import azure.functions as func

from shared.days_until import get_days_until


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Calculate days until next wednesday"""
    logging.info("Python HTTP trigger function processed a request.")

    msg, color = get_days_until(2)

    # return shield.io json
    return func.HttpResponse(
        json.dumps(
            {
                "schemaVersion": 1,
                "label": "days until wednesday",
                "message": msg,
                "color": color,
            }
        )
    )
