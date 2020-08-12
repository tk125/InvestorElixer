from django.urls                import include,path
from .                          import views
from django.conf                import settings
from django.conf.urls.static    import static

urlpatterns = [
    path('', views.index, name='index'),
    path('email_sent', views.email_sent, name='email_sent'),
    path('refreshAllStockPrice', views.refreshAllStockPrice, name='refreshAllStockPrice'),
    path('fiveYearSummary', views.fiveYearSummary, name='fiveYearSummary'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)