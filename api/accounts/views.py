from django.shortcuts import render
from rest_framework import permissions, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from commons import mixins as commons_mixins
from accounts import models as account_models
from accounts.serializers import ser as post_ser, get_ser
from api.utils.errors import Error
from api.utils.success import Success

class UserViewSet(commons_mixins.BaseViewsetMixin):

    queryset = account_models.User.objects.all()

    serializer_class = post_ser.SignupSerializer
    read_serializer_class = get_ser.UserViewSetSerializer

    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["username", "email", "is_deleted", "gender"]
    search_fields = ['username', 'email']
    ordering_fields = ["pk", "username", "email", "gender", "created_at", "is_deleted"]

    def get_queryset(self):
        return super().get_queryset()

    def get_detail_query(self, pk):
        
        try:
            user = account_models.User.objects.get(pk = pk)
            if user:
                return user
        except account_models.User.DoesNotExist:
            return None

    def list(self, request):

        user = self.filter_queryset(self.get_queryset())

        print(f"user : {user}")

        user_json = get_ser.UserViewSetSerializer(user, many=True)

        return Response({"message": user_json.data}, status = status.HTTP_200_OK)


    def create(self, request):
        
        new_user = post_ser.SignupSerializer(data = request.data)

        if new_user.is_valid():
            new_user.save()

            return Response(Success.response(self.__class__.__name__, request.method, "회원가입 완료", "201"), status = status.HTTP_201_CREATED)

        else:
            print(new_user.errors)
            return Response(Error.errors("에러"))

    def destroy(self, request, pk):

        user = account_models.User.objects.get(pk = pk)

        user.delete()

        return Response(Success.response(self.__class__.__name__, request.method, "삭제 완료", "200"), status = status.HTTP_200_OK)