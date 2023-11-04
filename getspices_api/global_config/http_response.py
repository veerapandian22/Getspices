from typing import Any
from rest_framework import status
from rest_framework.response import Response


def HTTP_OK(data: Any) -> Response:
    return Response(data, status=status.HTTP_200_OK)


def HTTP_CREATED(data: Any) -> Response:
    return Response(data, status=status.HTTP_201_CREATED)


def HTTP_ACCEPTED(data: Any) -> Response:
    return Response(data, status=status.HTTP_202_ACCEPTED)


def HTTP_BAD_REQUEST(data: Any) -> Response:
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


def HTTP_UNAUTHORIZED(data: Any) -> Response:
    return Response(data, status=status.HTTP_401_UNAUTHORIZED)


def HTTP_NOT_FOUND(data: Any) -> Response:
    return Response(data, status=status.HTTP_404_NOT_FOUND)


def HTTP_INTERNAL_SERVER_ERROR(data: Any) -> Response:
    return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def HTTP_403_FORBIDDEN(data: Any) -> Response:
    return Response(data, status=status.HTTP_403_FORBIDDEN)
