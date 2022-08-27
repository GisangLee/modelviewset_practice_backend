import os, jwt, datetime, time
from django.contrib.auth import get_user_model
from rest_framework import exceptions
import logging as log

JWT_SECRET = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("JWT_ALGORITHM")

server_logger = log.getLogger("django.request")

# JWT 발급 시스템
def generate_jwt_token(payload, type):
    SECONDS = 1
    MINUTE = SECONDS * 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24
    MONTH = DAY * 30
    YEAR = DAY * 365

    if type == "access":
        #exp = datetime.datetime.now() + datetime.timedelta(seconds=3)
        # 만료 토큰 생명 주기 한 달
        exp = int(time.time()) + (MONTH)

    elif type == "refresh":
        # 갱신 토큰 생명 주기 한 달 + 1주
        exp = int(time.time()) + (MONTH + (DAY * 7))

    else:
        raise Exception("토큰 타입을 정확하게 명시해 주세요.")

    payload["exp"] = exp
    payload["iat"] = datetime.datetime.now()
    jwt_encoded = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)

    return jwt_encoded




user_model = get_user_model()

def get_authorization_header(request):
    auth = request.META.get("HTTP_AUTHORIZATION")
    return auth

def get_system_key(request):
    system_key = request.META.get("HTTP_SYSTEM_KEY")
    print(f"system_key: {system_key}")
    return system_key


class CustomJwtTokenAuthentication(object):
    
    keyword = "jwt"

    def authenticate(self, request):
        token = get_authorization_header(request)

        server_logger.debug({
            "JWT": token,
        })

        if not token:
            raise exceptions.AuthenticationFailed("사용자를 인증할 수 없습니다.")
        
        token = token.replace("jwt ", "")
        
        # 토큰 디코딩
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])

        # 토큰 만료 데이터 파싱
        expire = payload.get("exp")

        # 현재 시간
        cur_date = int(time.time())
        
        # 토큰 만료 처리
        if cur_date > expire:
            return None
        
        # 유저 객체
        user_id = payload.get("user_id")

        if not user_id:
            return None
        
        try:
            user = user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            raise exceptions.AuthenticationFailed("사용자가 존재하지 않습니다.")
        
        return (user, token)
        
    def authenticate_header(self, request):
        return self.keyword


class SystemKeyAuth(object):

    keyword = "key"

    def authenticate(self, request):
        system_key = get_system_key(request)

        if not system_key:
            raise exceptions.AuthenticationFailed("시스템키가 필요합니다.")
            #return (0, 0)

        else:
            system_key = system_key.split(" ")[-1].strip()

            if system_key != os.environ.get("SYSTEM_KEY"):
                raise exceptions.AuthenticationFailed("시스템키가 필요합니다.")

            return (0, 0)


    def authenticate_header(self, request):

        return self.keyword