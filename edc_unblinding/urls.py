from django.urls.conf import path
from django.views.generic import RedirectView

app_name = "edc_unblinding"

urlpatterns = [
    path("", RedirectView.as_view(url="/edc_unblinding_admin/"), name="home_url"),
]
