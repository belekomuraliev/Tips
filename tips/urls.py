
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from interview import views

schema_view = get_schema_view(
    openapi.Info(
        title="Tips API",
        default_version='v0.1',
        description="API шпоргалка для интервью",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="boke74@mail.ru"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categorys/', views.CategoryCreateListAPIView.as_view()),
    path('api/categorys/<int:category_id>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/questions/', views.QuestionAnswerListCreateAPIView.as_view()),
    path('api/questions/<int:question_id>/', views.QuestionAnswerRetrieveUpdateDestroyAPIView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),
]
