""".

This is a sample product store API implemented using Google Cloud
Endpoints and datastore.

"""

import endpoints
from protorpc import remote
from models import Product


@endpoints.api(name='bicyclestore', version='v1', description='Bikestore API')
class ProductService(remote.Service):
    """Product service."""

    @Product.method(path='/product/', http_method='POST',
                    name='product.insert')
    def insert_product(self, product):
        """Insert a new product with the given body."""
        product.put()
        return product

    @Product.method(request_fields=('id',), path='/product/{id}',
                    http_method='GET', name='product.get')
    def get_product(self, product):
        """Get a product with the given id."""
        if not product.from_datastore:
            raise endpoints.NotFoundException('product not found.')
        return product

    @Product.method(name='product.update', path='/product/{id}',
                    http_method='PUT')
    def update_product(self, product):
        """Update an existent product with the given id and body."""
        if not product.from_datastore:
            raise endpoints.NotFoundException('product not found.')
        product.put()
        return product

    @Product.method(name='product.patch', path='/product/{id}',
                    http_method='PATCH')
    def patch_product(self, product):
        """Update an existent product with the given id and body.

        using patch method.
        """
        if not product.from_datastore:
            raise endpoints.NotFoundException('product not found.')
        product.put()
        return product

    @Product.method(request_fields=('id',),
                    response_fields=('id',), path='/product/{id}',
                    http_method='DELETE', name='product.delele')
    def delete_product(self, product):
        """Delete an existent product with the given id and body."""
        if not product.from_datastore:
            raise endpoints.NotFoundException('product not found.')
        product.key.delete()
        return product

    @Product.query_method(query_fields=('limit', 'pageToken'),
                          path='/products/', name='product.list')
    def list_products(self, query):
        """List all products with pagination."""
        return query
