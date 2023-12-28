from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 2 
    page_query_param = 'p'         #bydefault it's 'page'word
    page_size_query_param = 'size' #we can mention size per page in url eg ?size=10
    max_page_size = 3             #max elem per page if you pass ?size=4, it will still show 3
    # last_page_strings = 'end'     #redirect to last page eg. ?p=end 
    
class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5 #default limit for 1st page
    max_limit = 7
    
    
class WatchListCPagition(CursorPagination):
    page_size = 2
    ordering = 'created'