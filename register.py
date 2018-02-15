"""Endpoint api server registration."""

import endpoints
from services.product_service import ProductService

application = endpoints.api_server([ProductService])
