from django.urls import path
from .views import AdsCreate, AdsList, AdsDetail


urlpatterns = [
   path('', AdsList.as_view()),

   path('ads/', AdsList.as_view(), name='news_list'),
   path('ads/<int:pk>', AdsDetail.as_view(), name='a_ads'),

   path('ads/create/', AdsCreate.as_view(), name='ads_create'),
   # path('news/<int:pk>/edit/', NewsEdit.as_view(), name='post_edit'),
   # path('news/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete')
]