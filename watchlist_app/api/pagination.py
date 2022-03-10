from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 5
    #page_query_param = 'p' # To change the name
    page_size_query_param = 'size' #Custom page based on client request
    max_page_size = 10
    #last_page_strings = 'end' # to vist last page by the string
    
class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
    
class WatchListCursorPagination(CursorPagination):
    page_size= 5
    #cursor_query_param = 'record'
    ordering = 'created' #To odering the data based on created date and time