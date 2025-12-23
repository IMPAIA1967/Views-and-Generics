from rest_framework.pagination import PageNumberPagination


class MaterialsPagination(PageNumberPagination):
    page_size = 5  # Сколько объектов на одной странице по умолчанию
    page_size_query_param = 'page_size'  # Какой параметр использовать в URL
    max_page_size = 20  # Максимум, сколько можно запросить за раз