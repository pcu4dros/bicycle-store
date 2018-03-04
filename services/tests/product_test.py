""".

This is test file for product service, this file have the unit tests for the
service implementation.

"""

import unittest
import endpoints
import webtest

from google.appengine.ext import testbed
from models import Product
from services.product_service import ProductService


class ProductTestCase(unittest.TestCase):
    """API unit tests."""

    def setUp(self):
        """Configure the initial setup for tests."""
        tb = testbed.Testbed()
        tb.setup_env(current_version_id='testbed.version')
        tb.activate()
        tb.init_all_stubs()
        self.testbed = tb

        app = endpoints.api_server([ProductService], restricted=False)
        self.testapp = webtest.TestApp(app)

    def tearDown(self):
        """Deactivate the testbed tool at the end of the execution."""
        self.testbed.deactivate()

    def test_endpoint_get(self):
        """Test get endpoint of the service product."""
        product = Product(model='Diamondback Hook',
                          description="Diamondback the best Hook",
                          price=500.3,
                          photo="/images/model/01/diamondback-hook.png"
                          )
        product.put()

        response = self.testapp.get('/_ah/api/bicyclestore/v1/product/' +
                                    str(product.id))

        data = response.json

        self.assertEquals(response.status_code, 200)
        self.assertEquals(data['model'], 'Diamondback Hook')
        self.assertEquals(data['description'], 'Diamondback the best Hook')
        self.assertEquals(data['price'], 500.3)
        self.assertEquals(data['id'], str(product.key.id()))

    def test_endpoint_post(self):
        """Test update endpoint of the service product."""
        body = {"model": "Diamondback Hook",
                "photo": "/images/model/01/diamondback-hook.png",
                "price": 500.3,
                "description": "Diamondback the best Hook",
                "short_description": "Diamondback"}
        response = self.testapp.post_json('/_ah/api/bicyclestore/v1/product/',
                                          body)

        data = response.json

        self.assertEquals(response.status_code, 200)
        self.assertEquals(data['model'], 'Diamondback Hook')
        self.assertEquals(data['description'], 'Diamondback the best Hook')
        self.assertEquals(data['short_description'], 'Diamondback')
        self.assertEquals(data['price'], 500.3)

    def test_endpoint_update(self):
        """Test post endpoint of the service product."""
        product = Product(model='Diamondback Black',
                          description="Diamondback the worst Hook",
                          price=500.3,
                          photo="/images/model/01/diamondback.png"
                          )

        product.put()

        body = {"model": "Diamondback Hook",
                "photo": "/images/model/01/diamondback-hook.png",
                "price": 500.3,
                "description": "Diamondback the best Hook"}

        response = self.testapp.put_json('/_ah/api/bicyclestore/v1/product/' +
                                         str(product.key.id()), body)

        data = response.json

        self.assertEquals(response.status_code, 200)
        self.assertEquals(data['model'], 'Diamondback Hook')
        self.assertEquals(data['description'], 'Diamondback the best Hook')
        self.assertEquals(data['price'], 500.3)

    def test_endpoint_patch(self):
        """Test patch endpoint of the service product."""
        product = Product(model='Diamondback Black',
                          description="Diamondback the worst Hook",
                          price=500.3,
                          photo="/images/model/01/diamondback.png"
                          )

        product.put()

        body = {"model": "Diamondback Black",
                "price": 1000.3,
                "description": "Diamondback new generation"}

        response = self.testapp.patch_json('/_ah/api/bicyclestore/v1/product/'
                                           + str(product.key.id()), body)

        data = response.json

        self.assertEquals(response.status_code, 200)
        self.assertEquals(data['model'], 'Diamondback Black')
        self.assertEquals(data['description'], 'Diamondback new generation')
        self.assertEquals(data['price'], 1000.3)

    def test_endpoint_list(self):
        """Test list endpoint of the service product."""
        product = Product(model='Diamondback Hook',
                          description="Diamondback the best Hook",
                          price=500.3,
                          photo="/images/model/01/diamondback-hook.png"
                          )
        product.put()

        product2 = Product(model='Raleigh Revere',
                           description="Raleigh's Revere 1 womens road bike.",
                           price=700.0,
                           photo="/images/model/01/raleigh-revere.png"
                           )
        product2.put()

        # limit param is for pagination,show only two products for page
        response = self.testapp.get('/_ah/api/bicyclestore/v1/products/' +
                                    '?limit=2')

        data = response.json

        self.assertEquals(response.status_code, 200)
        self.assertEquals(data['items'][0]['model'], 'Diamondback Hook')
        self.assertEquals(data['items'][0]['description'],
                          'Diamondback the best Hook')
        self.assertEquals(data['items'][0]['price'], 500.3)
        self.assertEquals(data['items'][0]['id'], str(product.key.id()))
        self.assertEquals(data['items'][1]['model'], 'Raleigh Revere')
        self.assertEquals(data['items'][1]['description'],
                          "Raleigh's Revere 1 womens road bike.")
        self.assertEquals(data['items'][1]['price'], 700.0)
        self.assertEquals(data['items'][1]['id'], str(product2.key.id()))

    def test_endpoint_delete(self):
        """Test delete endpoint of the service product."""
        product = Product(model='Diamondback Black',
                          description="Diamondback the worst Hook",
                          price=500.3,
                          photo="/images/model/01/diamondback.png"
                          )

        product.put()

        response = self.testapp.delete('/_ah/api/bicyclestore/v1/product/' +
                                       str(product.key.id()))

        data = response.json

        self.assertEquals(response.status_code, 200)
        self.assertEquals(data['id'],  str(product.key.id()))

    def test_post_returns_400_if_bad_request(self):
        """Test the post endpoint with an empty body."""
        body = {}

        response = self.testapp.post_json('/_ah/api/bicyclestore/v1/product/',
                                          body, expect_errors=True)
        self.assertEquals(response.status_code, 400)

    def test_update_returns_404_if_id_not_exist(self):
        """Test update endpoint with an inexistent id."""
        body = {"model": "Diamondback Hook",
                "photo": "/images/model/01/diamondback-hook.png",
                "price": 500.3,
                "description": "Diamondback the best Hook"}

        id = '8881991222'

        response = self.testapp.put_json('/_ah/api/bicyclestore/v1/product/' +
                                         id, body,
                                         expect_errors=True)

        self.assertEquals(response.status_code, 404)

    def test_get_returns_404_if_no_entity(self):
        """Test get endpoint with an inexistent id."""
        id = '8881991222'

        response = self.testapp.get('/_ah/api/bicyclestore/v1/product/' + id,
                                    expect_errors=True)
        self.assertEquals(response.status_code, 404)

    def test_delete_returns_404_if_id_not_exist(self):
        """Test delete endpoint with an inexistent id."""
        product = Product(model='Diamondback Black',
                          description="Diamondback the worst Hook",
                          price=500.3,
                          photo="/images/model/01/diamondback.png"
                          )

        product.put()

        id = '8881991222'

        response = self.testapp.delete('/_ah/api/bicyclestore/v1/product/' +
                                       id, expect_errors=True)

        self.assertEquals(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
