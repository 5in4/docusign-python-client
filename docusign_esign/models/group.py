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


class Group(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, error_details=None, group_id=None, group_name=None, group_type=None, permission_profile_id=None, users=None):
        """
        Group - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error_details': 'ErrorDetails',
            'group_id': 'str',
            'group_name': 'str',
            'group_type': 'str',
            'permission_profile_id': 'str',
            'users': 'list[UserInfo]'
        }

        self.attribute_map = {
            'error_details': 'errorDetails',
            'group_id': 'groupId',
            'group_name': 'groupName',
            'group_type': 'groupType',
            'permission_profile_id': 'permissionProfileId',
            'users': 'users'
        }

        self._error_details = error_details
        self._group_id = group_id
        self._group_name = group_name
        self._group_type = group_type
        self._permission_profile_id = permission_profile_id
        self._users = users

    @property
    def error_details(self):
        """
        Gets the error_details of this Group.

        :return: The error_details of this Group.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this Group.

        :param error_details: The error_details of this Group.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def group_id(self):
        """
        Gets the group_id of this Group.
        The DocuSign group ID for the group.

        :return: The group_id of this Group.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this Group.
        The DocuSign group ID for the group.

        :param group_id: The group_id of this Group.
        :type: str
        """

        self._group_id = group_id

    @property
    def group_name(self):
        """
        Gets the group_name of this Group.
        The name of the group.

        :return: The group_name of this Group.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this Group.
        The name of the group.

        :param group_name: The group_name of this Group.
        :type: str
        """

        self._group_name = group_name

    @property
    def group_type(self):
        """
        Gets the group_type of this Group.
        The group type.

        :return: The group_type of this Group.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """
        Sets the group_type of this Group.
        The group type.

        :param group_type: The group_type of this Group.
        :type: str
        """

        self._group_type = group_type

    @property
    def permission_profile_id(self):
        """
        Gets the permission_profile_id of this Group.
        The ID of the permission profile associated with the group.

        :return: The permission_profile_id of this Group.
        :rtype: str
        """
        return self._permission_profile_id

    @permission_profile_id.setter
    def permission_profile_id(self, permission_profile_id):
        """
        Sets the permission_profile_id of this Group.
        The ID of the permission profile associated with the group.

        :param permission_profile_id: The permission_profile_id of this Group.
        :type: str
        """

        self._permission_profile_id = permission_profile_id

    @property
    def users(self):
        """
        Gets the users of this Group.
        

        :return: The users of this Group.
        :rtype: list[UserInfo]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this Group.
        

        :param users: The users of this Group.
        :type: list[UserInfo]
        """

        self._users = users

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
