import pyramid.httpexceptions as x

from pyramid.view import view_config
from pyramid.request import Request

from pypi_web.viewmodels.packages.package_details_viewmodel import PackageDetailsViewModel
from pypi_web.viewmodels.packages.popular_viewmodel import PopularPackageViewModel


@view_config(route_name='package_details',
             renderer='pypi_web:templates/packages/details.pt')
@view_config(route_name='package_details/',
             renderer='pypi_web:templates/packages/details.pt')
def details(request: Request):
    vm = PackageDetailsViewModel(request)
    if not vm.package:
        raise x.HTTPNotFound()

    return vm.to_dict()


# /{num}
@view_config(route_name='popular',
             renderer='pypi_web:templates/packages/popular.pt')
def popular(request: Request):
    vm = PopularPackageViewModel(request)
    if not (1 <= vm.num or vm.num <= 10):
        raise x.HTTPNotFound()

    return vm.to_dict()