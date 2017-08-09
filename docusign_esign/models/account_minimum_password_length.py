# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AccountMinimumPasswordLength(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, maximum_length=None, minimum_length=None):
        """
        AccountMinimumPasswordLength - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'maximum_length': 'str',
            'minimum_length': 'str'
        }

        self.attribute_map = {
            'maximum_length': 'maximumLength',
            'minimum_length': 'minimumLength'
        }

        self._maximum_length = maximum_length
        self._minimum_length = minimum_length

    @property
    def maximum_length(self):
        """
        Gets the maximum_length of this AccountMinimumPasswordLength.
        

        :return: The maximum_length of this AccountMinimumPasswordLength.
        :rtype: str
        """
        return self._maximum_length

    @maximum_length.setter
    def maximum_length(self, maximum_length):
        """
        Sets the maximum_length of this AccountMinimumPasswordLength.
        

        :param maximum_length: The maximum_length of this AccountMinimumPasswordLength.
        :type: str
        """

        self._maximum_length = maximum_length

    @property
    def minimum_length(self):
        """
        Gets the minimum_length of this AccountMinimumPasswordLength.
        

        :return: The minimum_length of this AccountMinimumPasswordLength.
        :rtype: str
        """
        return self._minimum_length

    @minimum_length.setter
    def minimum_length(self, minimum_length):
        """
        Sets the minimum_length of this AccountMinimumPasswordLength.
        

        :param minimum_length: The minimum_length of this AccountMinimumPasswordLength.
        :type: str
        """

        self._minimum_length = minimum_length

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
