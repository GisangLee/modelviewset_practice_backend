import logging as log
from django.shortcuts import render
from rest_framework import permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from commons import mixins as commons_mixins
from accounts import models as account_models
from accounts.serializers import ser as post_ser, get_ser
from api.utils.errors import Error
from api.utils.success import Success
from api.utils.perms import AllowAny, owner_only
from api.utils.jwt import CustomJwtTokenAuthentication, SystemKeyAuth
from api.utils.swaggers import accounts_api_doc

server_logger = log.getLogger("django.request")

class UserViewSet(commons_mixins.BaseViewsetMixin):

    queryset = account_models.User.objects.all()

    serializer_class = post_ser.UpdateUserSerializer
    post_serializer_class = post_ser.SignupSerializer
    read_serializer_class = get_ser.UserViewSetSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["username", "email", "gender"]
    search_fields = ['username', 'email']
    ordering_fields = ["pk", "username", "email", "gender", "created_at", "is_deleted"]

    #authentication_classes = [SystemKeyAuth]

    def get_queryset(self):
        return super().get_queryset()

    def get_detail_query(self, pk):
        
        try:
            user = account_models.User.objects.get(pk = pk)
            if user:
                return user
        except account_models.User.DoesNotExist:
            return None

    @swagger_auto_schema(manual_parameters=accounts_api_doc.login, tags = ["사용자 조회"], operation_description="성공 200, 데이터 없을 시 빈 리스트")
    def list(self, request):

        user = self.filter_queryset(self.get_queryset())
        user = list(user)

        server_logger.debug({
            "message": user
        })

        user_json = get_ser.UserViewSetSerializer(user, many=True)

        return Response({"message": user_json.data}, status = status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=accounts_api_doc.auth_api_param, tags = ["사용자 정보 부분 수정"], operation_description="성공 200")
    @method_decorator(owner_only, name="dispatch")
    def partial_update(self, request, *args, **kwargs):

        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=accounts_api_doc.auth_api_param, tags = ["사용자 정보 전부 수정"], operation_description="성공 200")
    @method_decorator(owner_only, name="dispatch")
    def update(self, request, *args, **kwargs):

        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=accounts_api_doc.auth_api_param, tags = ["회원가입"], operation_description="성공 201, 에러 400")
    def create(self, request):
        
        new_user = self.post_serializer_class(data = request.data)

        if new_user.is_valid():
            new_user.save()

            return Response(Success.response(self.__class__.__name__, request.method, "회원가입 완료", "201"), status = status.HTTP_201_CREATED)

        else:
            print(new_user.errors)
            return Response(Error.errors("에러"), status = status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=accounts_api_doc.auth_api_param, tags = ["데이터 물리 / 논리 삭제"], operation_description="성공 200")
    def destroy(self, request, pk):

        user = self.get_detail_query(pk)

        user.delete()

        return Response(Success.response(self.__class__.__name__, request.method, "삭제 완료", "200"), status = status.HTTP_200_OK)


class LoginView(APIView):

    permission_classes = [AllowAny]
    serializer_classes = post_ser.LoginSerializer
    #authentication_classes = [SystemKeyAuth]

    def post(self, request):

        user = self.serializer_classes(data = request.data)
        
        if user is None:
            return Response(Error.errors("로그인 실패"), status = status.HTTP_400_BAD_REQUEST)

        user_data = user.initial_data

        user_data.pop("password")

        return Response(Success.response(self.__class__.__name__, request.method, user_data, "200"))



