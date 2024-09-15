from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class SuccessResponse(Response):
    def __init__(self, data=None, status=HTTP_200_OK,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        super().__init__(
            {"data": data, "msg": "success", "code": 0},
            status,
            template_name,
            headers,
            exception,
            content_type
        )


class FailureResponse(Response):
    def __init__(self, err=None, code=400, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        super().__init__(
            {"data": None, "msg": err, "code": code},
            status,
            template_name,
            headers,
            exception,
            content_type
        )