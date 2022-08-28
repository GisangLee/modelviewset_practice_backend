import json, datetime, time
import pytest
from rest_framework import status
from rest_framework.reverse import reverse
import accounts.models as account_models

TOTAL_USERS = 0

@pytest.mark.urls(urls="config.urls")
@pytest.mark.django_db
def test_user_set(rf, client):
    
    url = reverse(viewname="accounts-list")

    response = client.get(url)

    data = json.loads(response.content)
    assert len(data.get("message")) == TOTAL_USERS
    assert response.status_code == status.HTTP_200_OK

    print(data)


@pytest.mark.urls(urls="config.urls")
@pytest.mark.django_db
def test_create_user_failiure(rf, client):
    
    url = reverse(viewname="accounts-list")

    not_enough_data = {
        "username": "테스트 계정 1",
        "password": "qwe123",
        "gender": "m",
        "age": 30,
    }
    response = client.post(url, data = not_enough_data)

    data = json.loads(response.content)

    assert data.get("errors") == "에러"
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    #print(data)

@pytest.mark.urls(urls="config.urls")
@pytest.mark.django_db
def test_create_user_success(rf, client):
    url = reverse(viewname="accounts-list")

    good_data = {
        "username": "테스트 계정 1",
        "email": "test@gmail.com",
        "password": "qwe123",
        "gender": "m",
        "age": 30,
    }

    response = client.post(url, data = good_data)

    data = json.loads(response.content)

    assert data.get("message") == "회원가입 완료"
    assert response.status_code == status.HTTP_201_CREATED

    print(data)

# @pytest.mark.urls(urls="config.urls")
# @pytest.mark.django_db
# def test_modify_user_failure(rf, client):
#     pk = 1
#     #url = reverse(viewname="accounts-detail")
#     url = "http://127.0.0.1:8000/api-v1/accounts/1/"

#     not_enough_data = {
#         "username": "테스트 계정 1",
#         "age": 30,
#     }

#     response = client.put(url, data = not_enough_data)
#     print(f"data raw : {response}")

#     #data = json.loads(response.content)
#     #print(f"data : {data}")
#     #assert data.get("message") == "회원가입 완료"
#     assert response.status_code == status.HTTP_400_BAD_REQUEST

    


# @pytest.mark.urls(urls="config.urls")
# @pytest.mark.django_db
# def test_modify_user_success(rf, client):
    
#     url = "http://127.0.0.1:8000/api-v1/accounts/1/"

#     good_data = {
#         "username": "테스트 계정 1",
#         "email": "test@gmail.com",
#         "phone_number": "010-1111-9999",
#         "gender": "m",
#         "age": 30,
#     }

#     response = client.put(url, data = good_data)

#     data = json.loads(response.content)
#     print(f"data : {data}")
#     assert data.get("message") == "회원가입 완료"
#     assert response.status_code == status.HTTP_200_OK