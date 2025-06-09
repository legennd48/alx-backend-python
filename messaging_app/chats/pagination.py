from rest_framework.pagination import PageNumberPagination

class StandardMessagePagination(PageNumberPagination):
    page_size = 20  # Fetch 20 messages per page
    page_size_query_param = 'page_size' # Optional: allow client to set page_size
    max_page_size = 100 # Optional: maximum page size client can request