from django.urls import path

from catalog.views import (
    DishDetailView,
    IndexView,
    DetailsView,
    BeverageListView,
    CreateDishView,
    DeleteDishView,
    UserDishesView,
    UpdateDishView,
    GuestPageView,
)

app_name = "catalog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("guest/", GuestPageView.as_view(), name="guest_page"),
    path("detail/<int:pk>/", DetailsView.as_view(), name="show_info"),
    path("add_comment/<int:pk>", DishDetailView.as_view(), name="detail"),
    path("beverages/", BeverageListView.as_view(), name="beverages"),
    # path('login/', CookLoginView.as_view(), name='cook_login'),
    path("create_dish/", CreateDishView.as_view(), name="create_dish"),
    path("delete_dish/<int:dish_id>/", DeleteDishView.as_view(), name="delete_dish"),
    path("users_dishes/<int:user_id>/", UserDishesView.as_view(), name="user_dishes"),
    path("update_dish/<int:pk>/", UpdateDishView.as_view(), name="update_dish"),
    # path('logout/', LogoutView.as_view(), name='logout'),
]
