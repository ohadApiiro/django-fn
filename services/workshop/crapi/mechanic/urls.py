from django.urls import include, re_path
import crapi.mechanic.views as mechanic_views

urlpatterns = [
    re_path(r"signup$", mechanic_views.SignUpView.as_view()),
    re_path(r"receive_report$", mechanic_views.ReceiveReportView.as_view()),
    re_path(
        r"mechanic_report$",
        mechanic_views.GetReportView.as_view(),
        name="get-mechanic-report",
    ),
    re_path(
        r"service_request/(?P<service_request_id>[0-9]+)/comment$",
        mechanic_views.ServiceCommentView.as_view(),
    ),
    re_path(
        r"service_request/(?P<service_request_id>[0-9]+)$",
        mechanic_views.ServiceRequestView.as_view(),
    ),
    re_path(r"service_requests$", mechanic_views.MechanicServiceRequestsView.as_view()),
    re_path(
        r"service_request$",
        mechanic_views.MechanicServiceRequestsView.as_view(),
    ),
    re_path(r"$", mechanic_views.MechanicView.as_view()),
]
