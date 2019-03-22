import unittest
import unittest.mock
import pyramid.testing

from pypi_web.data.packages import Package
from pypi_web.data.releases import Release


class PackageControllerTests(unittest.TestCase):
    def test_package_details_success(self):
        # Arrange
        request = pyramid.testing.DummyRequest()
        request.matchdict = {'package_name': 'sqlalchemy'}
        from pypi_web.controllers.packages_controller import details

        test_package = Package()
        test_package.id = 'sqlalchemy'
        test_package.releases = [
            Release(),
            Release(),
        ]

        # Act
        with unittest.mock.patch('pypi_web.services.package_service.find_package_by_name',
                                 return_value=test_package):
            model = details(request)

        # Assert
        package = model.get('package')
        self.assertIsNotNone(package)
        self.assertEqual(package.id, 'sqlalchemy')
