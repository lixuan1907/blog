from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 1
    page_size_query_param = 'size'
    page_query_param = 'page'

