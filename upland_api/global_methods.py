from json.decoder import JSONDecodeError
from json import loads


def verify_success(request, ok_code):
    """
    If the request is not successful, raise an exception

    :param request: The request object returned from the API call
    :param ok_code: The HTTP status code that indicates success
    """
    status_code = request.status_code
    response_text = request.text
    if status_code != ok_code:
        raise Exception(
            f"Request failed towards Upland, received {status_code}: {response_text}"
        )

    # Try to convert to json
    try:
        loads(request.text)
    except JSONDecodeError:
        raise Exception(
            f"Failed to convert JSON object, received following from Upland: {response_text}"
        )
    except TypeError:
        raise Exception(
            f"Failed to convert JSON object, received following from Upland: {response_text}"
        )
