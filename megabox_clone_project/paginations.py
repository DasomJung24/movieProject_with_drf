from urllib.parse import urlparse, parse_qsl
from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'per_page'

    def get_only_pagenumber(self, url):
        res = urlparse(url)
        queryset = dict(parse_qsl(res.query))

        result = queryset.get('page', None)

        if result:
            result = int(result)

        return result

    def get_paginated_response(self, data):

        return Response({
            'next': self.get_only_pagenumber(self.get_next_link()),
            'prev': self.get_only_pagenumber(self.get_previous_link()),
            'count': self.page.paginator.count,
            'results': data
        })
