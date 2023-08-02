from abc import abstractmethod

from PySide6.QtNetwork import QNetworkReply

from ..utils import ABCQObject


class ApiInterface(ABCQObject):
    # An abstract base class representing the interface for API operations.

    @abstractmethod
    def create(self, *args, **kwargs) -> QNetworkReply:...
        # Abstract method for creating a new resource.

    @abstractmethod
    def read(self, *args, **kwargs) -> QNetworkReply:...
        # Abstract method for reading a resource.

    @abstractmethod
    def update(self, *args, **kwargs) -> QNetworkReply:...
        # Abstract method for updating a resource.

    @abstractmethod
    def delete(self, *args, **kwargs) -> QNetworkReply:...
        # Abstract method for deleteing a resource.
