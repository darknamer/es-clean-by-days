import json

import requests


def get_log_later_days(domain: str, indices: str, days: int = 7):
    url = f"{domain}/{indices}/_search"
    payload = json.dumps({
        "query": {
            "range": {
                "timestamp": {
                    "lt": f"now-{days}d/d"
                }
            }
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def delete_log_by_id(domain: str, indices: str, id: str):
    url = f"{domain}/{indices}/_doc/{id}"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers)
    return response.text


def delete_log_later_days(domain: str, indices: str, days: int):
    url = f"{domain}/{indices}/_delete_by_query"
    payload = json.dumps({
        "query": {
            "range": {
                "timestamp": {
                    "lt": f"now-{days}d/d"
                }
            }
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
