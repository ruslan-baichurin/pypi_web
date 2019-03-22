from pyramid.request import Request

from pypi_web.services import user_service
from pypi_web.viewmodels.shared.viewmodel_base import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.email = self.request_dict.get('email')
        self.name = self.request_dict.get('name')
        self.password = self.request_dict.get('password')

        if self.email:
            self.email = self.email.strip().lower()

        if self.name:
            self.name = self.name.strip()

    def validate(self):
        if not self.email:
            self.error = 'You must specify an email address'
        elif not self.name:
            self.error = 'You must specify your name'
        elif not self.password:
            self.error = 'You must specify a password'

        if user_service.find_user_by_email(self.email):
            self.error = "This user already exists"
