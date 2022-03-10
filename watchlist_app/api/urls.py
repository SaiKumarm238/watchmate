from django.urls import path
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (ReviewCreate, Watch_Catch_ListAV, WatchDetailAV,WatchListAV , StreamPlatformAV, 
                                    StreamPlatformDetailAV, ReviewList, ReviewDetail,UserReview, WatchListLAV)

# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('<int:pk>', movie_details, name='movie-detail'),
# ]

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(), name="stream" ),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name="stream-detail"),

    # path('stream/<int:pk>/review', StreamPlatformDetailAV.as_view(), name="stream-detail"),
    # path('stream/review/<int:pk>', ReviewDetail.as_view(), name="review-detail"),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/reviews/', ReviewList.as_view(), name="review"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
    #path('cache_list/', Watch_Catch_ListAV.as_view(), name="cache_list"),
    #path('reviews/<str:username>/', UserReview.as_view(), name="user-review-detail"),
    path('reviews/', UserReview.as_view(), name="user-review-detail"),
    # Filtering & Search
    path('listfs/', WatchListLAV.as_view(), name="movie-list-f-s"),
    
]
