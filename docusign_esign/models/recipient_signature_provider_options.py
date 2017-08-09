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


class RecipientSignatureProviderOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cpf_number=None, one_time_password=None, signer_role=None, sms=None):
        """
        RecipientSignatureProviderOptions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cpf_number': 'str',
            'one_time_password': 'str',
            'signer_role': 'str',
            'sms': 'str'
        }

        self.attribute_map = {
            'cpf_number': 'cpfNumber',
            'one_time_password': 'oneTimePassword',
            'signer_role': 'signerRole',
            'sms': 'sms'
        }

        self._cpf_number = cpf_number
        self._one_time_password = one_time_password
        self._signer_role = signer_role
        self._sms = sms

    @property
    def cpf_number(self):
        """
        Gets the cpf_number of this RecipientSignatureProviderOptions.
        

        :return: The cpf_number of this RecipientSignatureProviderOptions.
        :rtype: str
        """
        return self._cpf_number

    @cpf_number.setter
    def cpf_number(self, cpf_number):
        """
        Sets the cpf_number of this RecipientSignatureProviderOptions.
        

        :param cpf_number: The cpf_number of this RecipientSignatureProviderOptions.
        :type: str
        """

        self._cpf_number = cpf_number

    @property
    def one_time_password(self):
        """
        Gets the one_time_password of this RecipientSignatureProviderOptions.
        

        :return: The one_time_password of this RecipientSignatureProviderOptions.
        :rtype: str
        """
        return self._one_time_password

    @one_time_password.setter
    def one_time_password(self, one_time_password):
        """
        Sets the one_time_password of this RecipientSignatureProviderOptions.
        

        :param one_time_password: The one_time_password of this RecipientSignatureProviderOptions.
        :type: str
        """

        self._one_time_password = one_time_password

    @property
    def signer_role(self):
        """
        Gets the signer_role of this RecipientSignatureProviderOptions.
        

        :return: The signer_role of this RecipientSignatureProviderOptions.
        :rtype: str
        """
        return self._signer_role

    @signer_role.setter
    def signer_role(self, signer_role):
        """
        Sets the signer_role of this RecipientSignatureProviderOptions.
        

        :param signer_role: The signer_role of this RecipientSignatureProviderOptions.
        :type: str
        """

        self._signer_role = signer_role

    @property
    def sms(self):
        """
        Gets the sms of this RecipientSignatureProviderOptions.
        

        :return: The sms of this RecipientSignatureProviderOptions.
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """
        Sets the sms of this RecipientSignatureProviderOptions.
        

        :param sms: The sms of this RecipientSignatureProviderOptions.
        :type: str
        """

        self._sms = sms

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
