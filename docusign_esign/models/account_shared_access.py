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


class AccountSharedAccess(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account_id=None, end_position=None, error_details=None, next_uri=None, previous_uri=None, result_set_size=None, shared_access=None, start_position=None, total_set_size=None):
        """
        AccountSharedAccess - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_id': 'str',
            'end_position': 'str',
            'error_details': 'ErrorDetails',
            'next_uri': 'str',
            'previous_uri': 'str',
            'result_set_size': 'str',
            'shared_access': 'list[MemberSharedItems]',
            'start_position': 'str',
            'total_set_size': 'str'
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'end_position': 'endPosition',
            'error_details': 'errorDetails',
            'next_uri': 'nextUri',
            'previous_uri': 'previousUri',
            'result_set_size': 'resultSetSize',
            'shared_access': 'sharedAccess',
            'start_position': 'startPosition',
            'total_set_size': 'totalSetSize'
        }

        self._account_id = account_id
        self._end_position = end_position
        self._error_details = error_details
        self._next_uri = next_uri
        self._previous_uri = previous_uri
        self._result_set_size = result_set_size
        self._shared_access = shared_access
        self._start_position = start_position
        self._total_set_size = total_set_size

    @property
    def account_id(self):
        """
        Gets the account_id of this AccountSharedAccess.
        The account ID associated with the envelope.

        :return: The account_id of this AccountSharedAccess.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this AccountSharedAccess.
        The account ID associated with the envelope.

        :param account_id: The account_id of this AccountSharedAccess.
        :type: str
        """

        self._account_id = account_id

    @property
    def end_position(self):
        """
        Gets the end_position of this AccountSharedAccess.
        The last position in the result set. 

        :return: The end_position of this AccountSharedAccess.
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """
        Sets the end_position of this AccountSharedAccess.
        The last position in the result set. 

        :param end_position: The end_position of this AccountSharedAccess.
        :type: str
        """

        self._end_position = end_position

    @property
    def error_details(self):
        """
        Gets the error_details of this AccountSharedAccess.

        :return: The error_details of this AccountSharedAccess.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this AccountSharedAccess.

        :param error_details: The error_details of this AccountSharedAccess.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def next_uri(self):
        """
        Gets the next_uri of this AccountSharedAccess.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :return: The next_uri of this AccountSharedAccess.
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """
        Sets the next_uri of this AccountSharedAccess.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :param next_uri: The next_uri of this AccountSharedAccess.
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """
        Gets the previous_uri of this AccountSharedAccess.
        The postal code for the billing address.

        :return: The previous_uri of this AccountSharedAccess.
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """
        Sets the previous_uri of this AccountSharedAccess.
        The postal code for the billing address.

        :param previous_uri: The previous_uri of this AccountSharedAccess.
        :type: str
        """

        self._previous_uri = previous_uri

    @property
    def result_set_size(self):
        """
        Gets the result_set_size of this AccountSharedAccess.
        The number of results returned in this response. 

        :return: The result_set_size of this AccountSharedAccess.
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """
        Sets the result_set_size of this AccountSharedAccess.
        The number of results returned in this response. 

        :param result_set_size: The result_set_size of this AccountSharedAccess.
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def shared_access(self):
        """
        Gets the shared_access of this AccountSharedAccess.
        A complex type containing the shared access information to an envelope for the users specified in the request.

        :return: The shared_access of this AccountSharedAccess.
        :rtype: list[MemberSharedItems]
        """
        return self._shared_access

    @shared_access.setter
    def shared_access(self, shared_access):
        """
        Sets the shared_access of this AccountSharedAccess.
        A complex type containing the shared access information to an envelope for the users specified in the request.

        :param shared_access: The shared_access of this AccountSharedAccess.
        :type: list[MemberSharedItems]
        """

        self._shared_access = shared_access

    @property
    def start_position(self):
        """
        Gets the start_position of this AccountSharedAccess.
        Starting position of the current result set.

        :return: The start_position of this AccountSharedAccess.
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """
        Sets the start_position of this AccountSharedAccess.
        Starting position of the current result set.

        :param start_position: The start_position of this AccountSharedAccess.
        :type: str
        """

        self._start_position = start_position

    @property
    def total_set_size(self):
        """
        Gets the total_set_size of this AccountSharedAccess.
        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.

        :return: The total_set_size of this AccountSharedAccess.
        :rtype: str
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """
        Sets the total_set_size of this AccountSharedAccess.
        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.

        :param total_set_size: The total_set_size of this AccountSharedAccess.
        :type: str
        """

        self._total_set_size = total_set_size

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
