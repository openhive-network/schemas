import json


def check_json(_checker, instance):
    if isinstance(instance, str):
        try:
            if isinstance(json.loads(instance), dict):
                return True
        except ValueError:
            return False
    return False
