# coding: utf-8

"""
    SIGNATE API

    API for Public  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Download(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_id': 'int',
        'name': 'str',
        'url': 'str',
        'size': 'int',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'file_id': 'fileId',
        'name': 'name',
        'url': 'url',
        'size': 'size',
        'updated_at': 'updated_at'
    }

    def __init__(self, file_id=None, name=None, url=None, size=None, updated_at=None):  # noqa: E501
        """Download - a model defined in Swagger"""  # noqa: E501

        self._file_id = None
        self._name = None
        self._url = None
        self._size = None
        self._updated_at = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if size is not None:
            self.size = size
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def file_id(self):
        """Gets the file_id of this Download.  # noqa: E501


        :return: The file_id of this Download.  # noqa: E501
        :rtype: int
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this Download.


        :param file_id: The file_id of this Download.  # noqa: E501
        :type: int
        """

        self._file_id = file_id

    @property
    def name(self):
        """Gets the name of this Download.  # noqa: E501


        :return: The name of this Download.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Download.


        :param name: The name of this Download.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this Download.  # noqa: E501


        :return: The url of this Download.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Download.


        :param url: The url of this Download.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def size(self):
        """Gets the size of this Download.  # noqa: E501


        :return: The size of this Download.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Download.


        :param size: The size of this Download.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def updated_at(self):
        """Gets the updated_at of this Download.  # noqa: E501


        :return: The updated_at of this Download.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Download.


        :param updated_at: The updated_at of this Download.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Download, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Download):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
