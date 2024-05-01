from ninja_extra import NinjaExtraAPI
from django.contrib.admin.views.decorators import staff_member_required
from stations.api import router as stations_router

api = NinjaExtraAPI(
    title="Route Radar API",
    description="API consumed by FE client",
    version="0.1.0",
    urls_namespace="coreapi",
    docs_decorator=staff_member_required,
)

api.add_router("", stations_router)
