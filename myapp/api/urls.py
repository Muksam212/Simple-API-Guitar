from django.urls import path
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns =[ 
    path('band/api/create', BandCreate.as_view(), name="band_create"),
    path('band/api/list', BandList.as_view(), name="band_list"),
    path('band/api/<int:id>/update', BandUpdate.as_view(), name="band_update"),
    path('band/api/<int:id>/delete', BandDelete.as_view(), name="band_delete"),
    

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('member/api/create', BandMemberCreate.as_view(), name="band_member_create"),
    path('member/api/list', BandMemberList.as_view(), name="band_member_list"),
    path('member/api/<int:id>/update', BandMemberUpdate.as_view(), name="band_member_update"),
    path('member/api/<int:id>/delete', BandMemberDelete.as_view(), name="band_members_delete"),

    path('guitar/api/create', GuitarCreate.as_view(), name="guitar_create"),
    path('guitar/api/list', GuitarList.as_view(), name="guitar_list"),


]