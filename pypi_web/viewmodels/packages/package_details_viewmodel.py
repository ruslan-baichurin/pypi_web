from pyramid.request import Request

from pypi_web.services import package_service
from pypi_web.viewmodels.shared.viewmodel_base import ViewModelBase


class PackageDetailsViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.package_name = request.matchdict.get('package_name')
        self.package = package_service.find_package_by_name(self.package_name)

        self.latest_version = '0.0.0'
        self.latest_release = None

        if self.package and self.package.releases:
            self.latest_release = self.package.releases[0]
            self.latest_version = '{}.{}.{}'.format(
                self.latest_release.major_ver,
                self.latest_release.minor_ver,
                self.latest_release.build_ver
            )

        self.release_version = self.latest_version
        self.maintainers = []
        self.is_latest = True
