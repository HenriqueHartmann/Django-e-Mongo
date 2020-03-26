import pytest
from django.urls import reverse
from rest_framework import status

from DjangoMongo.core.models import Task


# POST
@pytest.mark.django_db
def test_create_valid(api_client):
    data_task = {"title": "Limpar 2", "description": "Limpar banheiros"}
    resp = api_client.post(reverse("task-list"), data_task)
    assert resp.status_code == status.HTTP_201_CREATED
    assert isinstance(resp.data["id"], str)
    assert Task.objects.get(pk=resp.data["id"]).title == data_task["title"]
    api_client.delete(reverse("task-detail", args={resp.data["id"]}))


@pytest.mark.django_db
def test_create_invalid(api_client):
    data_task = {"titla": "Limpar Banheiros"}
    resp = api_client.post(reverse("task-list"), data_task)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert len(resp.data["title"]) != 0


# GET - list
@pytest.mark.django_db
def test_list_valid(api_client):
    resp = api_client.get(reverse("task-list"))
    assert resp.status_code == status.HTTP_200_OK


# GET - retrieve
@pytest.mark.django_db
def test_retrieve_valid(api_client):
    task = Task.objects.create(title="Varrer", description="Retirar o pó com uma vassoura")
    resp = api_client.get(reverse("task-detail", args={task.id}))
    assert resp.status_code == status.HTTP_200_OK
    api_client.delete(reverse("task-detail", args={task.id}))


# PUT
@pytest.mark.django_db
def test_update_valid(api_client):
    task = Task.objects.create(title="Varrer", description="Retirar o pó com uma vassoura")
    data_task = {"title": "Varrer o piso"}
    resp = api_client.put(reverse("task-detail", args={task.id}), data_task)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data["title"] == "Varrer o piso"
    api_client.delete(reverse("task-detail", args={task.id}))


# DELETE
@pytest.mark.django_db
def test_destroy_valid(api_client):
    task = Task.objects.create(title="Varrer", description="Retirar o pó com uma vassoura")
    resp = api_client.delete(reverse("task-detail", args={task.id}))
    assert resp.status_code == status.HTTP_204_NO_CONTENT
