import math
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication


class ApiAuthMixin:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class AuthenticedModelViewSet(ApiAuthMixin, ModelViewSet):
    class Meta:
        abstract = True


class BasePagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    pass

    def get_paginated_response(self, data):
        # if you want to show page size in resposne just add these 2 lines
        if self.request.query_params.get("page_size"):
            self.page_size = int(self.request.query_params.get("page_size"))

        # you can count total page from request by total and page_size
        total_page = math.ceil(self.page.paginator.count / self.page_size)

        # here is your response
        return Response(
            {
                "count": self.page.paginator.count,
                "total": total_page,
                "previous": self.get_previous_link(),
                "next": self.get_next_link(),
                "results": data,
            }
        )


class BaseModelViewSet(AuthenticedModelViewSet):
    pagination_class = BasePagination

    def get_queryset(self):
        return self.queryset.filter(deleted=False).order_by("-created_at")

    def perform_destroy(self, instance):
        instance.soft_delete()

    class Meta:
        abstract = True
