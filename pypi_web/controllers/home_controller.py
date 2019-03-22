from pyramid.view import view_config

from pypi_web.viewmodels.home.home_index_viewmodel import HomeIndexViewModel
from pypi_web.viewmodels.shared.viewmodel_base import ViewModelBase


@view_config(route_name='home', renderer='pypi_web:templates/home/index.pt')
def home_index(request):
    vm = HomeIndexViewModel(request)
    return vm.to_dict()


@view_config(route_name='about', renderer='pypi_web:templates/home/about.pt')
def home_about(request):
    vm = ViewModelBase(request)
    return vm.to_dict()