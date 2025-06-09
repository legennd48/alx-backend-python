from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class StandardMessagePagination(PageNumberPagination):
    page_size = 20  # Fetch 20 messages per page
    page_size_query_param = 'page_size' # Optional: allow client to set page_size
    max_page_size = 100 # Optional: maximum page size client can request

    def get_paginated_response(self, data):
        # This structure ensures "page.paginator.count" is used.
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count, # Expected: "page.paginator.count"
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'page_size': self.get_page_size(self.request),
            'results': data
        })