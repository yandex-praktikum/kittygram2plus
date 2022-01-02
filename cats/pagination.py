from rest_framework import PageNumberPagination


class CatsPagination(PageNumberPagination):
    page_size = 20
