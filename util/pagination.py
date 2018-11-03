from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    """
    Pagination class
    """
    page_size_query_param = "size"
    max_page_size = 100
    page_size = 20
