import os
from drf_yasg import openapi

def make_api_param(name, type, desc, format, default=""):
    param = openapi.Parameter(
        name,
        type,
        description=desc,
        type=format,
        default=default
    )

    return param

base_api_param = [
    make_api_param("username", openapi.IN_QUERY, "필터링 검색", openapi.TYPE_STRING),
    make_api_param("email", openapi.IN_QUERY, "필터링 검색", openapi.TYPE_STRING),
    make_api_param("gender", openapi.IN_QUERY, "필터링 검색", openapi.TYPE_STRING),

    make_api_param("search", openapi.IN_QUERY, "검색 ( username, email 필드에서 검색 ) ", openapi.TYPE_STRING),

    make_api_param("ordering", openapi.IN_QUERY, "pk, username, email, gender, created_at, is_deleted", openapi.TYPE_STRING),
]

auth_api_param = [
    make_api_param("system_key", openapi.IN_HEADER, "시스템 key", openapi.FORMAT_INT64, default=f"key {os.environ.get('SECRET_KEY')}"),
    make_api_param("Authorization", openapi.IN_HEADER, "jwt", openapi.TYPE_STRING),
]

login = base_api_param + auth_api_param