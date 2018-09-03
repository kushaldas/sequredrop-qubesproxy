import os
import json
from subprocess import PIPE, Popen
from typing import List

from sdclientapi import Source, Submission


def json_query(data):
    """
    Takes a json based query and passes to the network proxy.
    Returns the JSON output from the proxy.
    """
    if os.path.exists("/etc/sd-proxy-vmname.conf"):
        with open("/etc/sd-proxy-vmname.conf") as fobj:           
            proxyvmname = fobj.read().strip()
    else:
        raise Exception("Missing /etc/sd-proxy-vmname.conf")
    p = Popen(
        ["/usr/lib/qubes/qrexec-client-vm", proxyvmname, "qubes.SDProxy"],
        stdin=PIPE,
        stdout=PIPE,
    )
    p.stdin.write(data.encode("utf-8"))
    d = p.communicate()
    output = d[0].decode("utf-8")
    return output.strip()


def login(username: str, password: str, otp: str) -> str:
    """
    Returns the authenticated token in JSON if the login is successful.
    Otherwise raises error.

    :param username: journalist username
    :param password: journalist password
    :param otp: Current OTP pin

    :returns: String representation of the JSON token. 
    """
    data = {
        "command": "login",
        "data": {"username": username, "password": password, "otp": otp},
    }
    result = json_query(json.dumps(data))

    resultd = json.loads(result)
    if "error" in resultd:
        raise Exception("Authentication Error")

    return result


def get_all_sources_json(token):
    """
    Returns a json object for all sources.

    :param token: string token for authentication

    :returns: String representation of the JSON list of sources
    """
    data = {"command": "get_all_sources", "data": token}

    result = json_query(json.dumps(data))

    return result


def get_all_sources(token: str) -> List[Source]:
    """
    Returns a list of Python Source objects
    """
    result = get_all_sources_json(token)
    result = json.loads(result)
    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])
    return [Source(**data) for data in result]


def get_source_json(token, uuid):
    """
    Returns a json object for a given source based on uuid.

    :param token: string token for authentication
    :param uuid: string uuid value of the source

    :returns: String representation of the JSON source
    """
    data = {"command": "get_source", "data": {"token": token, "uuid": uuid}}

    result = json_query(json.dumps(data))

    return result


def get_source(token: str, uuid: str) -> Source:
    """
    Returns an updated source object

    :param uuid: String uuid of a source

    :returns: An updated source object.
    """
    result = get_source_json(token, uuid)
    result = json.loads(result)
    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])
    return Source(**result)


def delete_source(token: str, uuid: str) -> bool:
    """
    Deletes a given source uuid.

    :param token: string token for authentication
    :param uuid: string uuid value of the source

    :returns: True or raises error.
    """
    data = {"command": "delete_source", "data": {"token": token, "uuid": uuid}}

    result = json_query(json.dumps(data))
    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])
    return json.loads(result)


def get_submissions_json(token, uuid):
    """
    Returns a json object for all submissions for a given source..

    :param token: string token for authentication

    :returns: String representation of the JSON list of submissions
    """
    data = {"command": "get_submissions", "data": {"token": token, "uuid": uuid}}

    result = json_query(json.dumps(data))

    return result


def get_submissions(token: str, uuid: str) -> List[Submission]:
    """
    Returns a list of Python Submission objects
    """
    result = get_submissions_json(token, uuid)
    result = json.loads(result)
    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])
    return [Submission(**data) for data in result]


def add_star(token: str, uuid: str) -> bool:
    """
    Adds a star to a given source uuid
    """
    data = {"command": "add_star", "data": {"token": token, "uuid": uuid}}

    result = json_query(json.dumps(data))
    result = json.loads(result)

    if type(result) == bool:
        return result

    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])


def remove_star(token: str, uuid: str) -> bool:
    """
    Removes a star to a given source uuid
    """
    data = {"command": "remove_star", "data": {"token": token, "uuid": uuid}}

    result = json_query(json.dumps(data))
    result = json.loads(result)

    if type(result) == bool:
        return result

    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])


def get_submission_json(token: str, uuid: str, source_uuid: str) -> str:
    """
    Returns the JSON reprentation of the submission object from the server

    :param token: token string
    :param uuid: submission uuid string
    :param source_uuid: source uuid string

    :returns: JSON representation of the submission object
    """
    data = {
        "command": "get_submission",
        "data": {"token": token, "uuid": uuid, "source_uuid": source_uuid},
    }

    result = json_query(json.dumps(data))

    return result


def get_submission(token: str, uuid: str, source_uuid: str) -> List[Submission]:
    """
    Returns a Submission object.
    
    :param token: token string
    :param uuid: submission uuid string
    :param source_uuid: source uuid string
    
    :returns: Submission object
    """
    result = get_submission_json(token, uuid, source_uuid)
    result = json.loads(result)
    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])
    return Submission(**result)


def get_all_submissions_json(token):
    """
    Returns a json object for all submissions.

    :param token: string token for authentication

    :returns: String representation of the JSON list of submissions
    """
    data = {"command": "get_all_submissions", "data": {"token": token}}

    result = json_query(json.dumps(data))

    return result


def get_all_submissions(token: str) -> List[Submission]:
    """
    Returns a list of Python Submission objects
    """
    result = get_all_submissions_json(token)
    result = json.loads(result)
    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])
    return [Submission(**data) for data in result]


def delete_submission(token: str, uuid: str, source_uuid: str) -> bool:
    """
    Deletes a submission object based on uuid.
    
    :param token: token string
    :param uuid: submission uuid string
    :param source_uuid: source uuid string
    
    :returns: True if operation successful.
    """
    data = {
        "command": "delete_submission",
        "data": {"token": token, "uuid": uuid, "source_uuid": source_uuid},
    }

    result = json_query(json.dumps(data))
    result = json.loads(result)

    if type(result) == bool:
        return result

    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])


def flag_source(token: str, uuid: str) -> bool:
    """
    Flags given source uuid
    """
    data = {"command": "flag_source", "data": {"token": token, "uuid": uuid}}

    result = json_query(json.dumps(data))
    result = json.loads(result)

    if type(result) == bool:
        return result

    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])

def get_current_user(token):
    """
    Returns a dict representation of the current user.
    """
    data = {"command": "get_current_user", "data": {"token": token}}

    result = json_query(json.dumps(data))
    result = json.loads(result)

    if "sdproxyerror" in result:
        raise Exception(result["sdproxyerror"])

    return result
