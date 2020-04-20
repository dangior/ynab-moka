# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SaveCategoryResponseData(object):
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
        'category': 'Category',
        'server_knowledge': 'int'
    }

    attribute_map = {
        'category': 'category',
        'server_knowledge': 'server_knowledge'
    }

    def __init__(self, category=None, server_knowledge=None):  # noqa: E501
        """SaveCategoryResponseData - a model defined in Swagger"""  # noqa: E501

        self._category = None
        self._server_knowledge = None
        self.discriminator = None

        self.category = category
        self.server_knowledge = server_knowledge

    @property
    def category(self):
        """Gets the category of this SaveCategoryResponseData.  # noqa: E501


        :return: The category of this SaveCategoryResponseData.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SaveCategoryResponseData.


        :param category: The category of this SaveCategoryResponseData.  # noqa: E501
        :type: Category
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def server_knowledge(self):
        """Gets the server_knowledge of this SaveCategoryResponseData.  # noqa: E501

        The knowledge of the server  # noqa: E501

        :return: The server_knowledge of this SaveCategoryResponseData.  # noqa: E501
        :rtype: int
        """
        return self._server_knowledge

    @server_knowledge.setter
    def server_knowledge(self, server_knowledge):
        """Sets the server_knowledge of this SaveCategoryResponseData.

        The knowledge of the server  # noqa: E501

        :param server_knowledge: The server_knowledge of this SaveCategoryResponseData.  # noqa: E501
        :type: int
        """
        if server_knowledge is None:
            raise ValueError("Invalid value for `server_knowledge`, must not be `None`")  # noqa: E501

        self._server_knowledge = server_knowledge

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
        if issubclass(SaveCategoryResponseData, dict):
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
        if not isinstance(other, SaveCategoryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
