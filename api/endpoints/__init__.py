from sanic import Blueprint

from .health.health import Health, HealthProtected
from .freshdesk.quotes import Quote
from .freshdesk.claims import Claim
from .freshdesk.emergencies import Emergency
from .freshdesk.contacts import Contact
from .freshdesk.policies import Policy
from .freshdesk.renewal import Renewal

health_blueprint = Blueprint(
    name="health",
    url_prefix="",
    version="v1",
    strict_slashes=True,
)   # /v1/health
health_blueprint.add_route(Health.as_view(), "/health", strict_slashes=True)
health_blueprint.add_route(HealthProtected.as_view(), "/health/protected", strict_slashes=True)
