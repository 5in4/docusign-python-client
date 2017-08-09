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


class UserInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account_management_granular=None, activation_access_code=None, created_date_time=None, custom_settings=None, email=None, enable_connect_for_user=None, error_details=None, first_name=None, forgotten_password_info=None, group_list=None, home_address=None, initials_image_uri=None, is_admin=None, last_login=None, last_name=None, login_status=None, middle_name=None, password=None, password_expiration=None, permission_profile_id=None, permission_profile_name=None, profile_image_uri=None, send_activation_on_invalid_login=None, signature_image_uri=None, suffix_name=None, title=None, uri=None, user_id=None, user_name=None, user_profile_last_modified_date=None, user_settings=None, user_status=None, user_type=None, work_address=None):
        """
        UserInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_management_granular': 'UserAccountManagementGranularInformation',
            'activation_access_code': 'str',
            'created_date_time': 'str',
            'custom_settings': 'list[NameValue]',
            'email': 'str',
            'enable_connect_for_user': 'str',
            'error_details': 'ErrorDetails',
            'first_name': 'str',
            'forgotten_password_info': 'ForgottenPasswordInformation',
            'group_list': 'list[Group]',
            'home_address': 'AddressInformationV2',
            'initials_image_uri': 'str',
            'is_admin': 'str',
            'last_login': 'str',
            'last_name': 'str',
            'login_status': 'str',
            'middle_name': 'str',
            'password': 'str',
            'password_expiration': 'str',
            'permission_profile_id': 'str',
            'permission_profile_name': 'str',
            'profile_image_uri': 'str',
            'send_activation_on_invalid_login': 'str',
            'signature_image_uri': 'str',
            'suffix_name': 'str',
            'title': 'str',
            'uri': 'str',
            'user_id': 'str',
            'user_name': 'str',
            'user_profile_last_modified_date': 'str',
            'user_settings': 'list[NameValue]',
            'user_status': 'str',
            'user_type': 'str',
            'work_address': 'AddressInformationV2'
        }

        self.attribute_map = {
            'account_management_granular': 'accountManagementGranular',
            'activation_access_code': 'activationAccessCode',
            'created_date_time': 'createdDateTime',
            'custom_settings': 'customSettings',
            'email': 'email',
            'enable_connect_for_user': 'enableConnectForUser',
            'error_details': 'errorDetails',
            'first_name': 'firstName',
            'forgotten_password_info': 'forgottenPasswordInfo',
            'group_list': 'groupList',
            'home_address': 'homeAddress',
            'initials_image_uri': 'initialsImageUri',
            'is_admin': 'isAdmin',
            'last_login': 'lastLogin',
            'last_name': 'lastName',
            'login_status': 'loginStatus',
            'middle_name': 'middleName',
            'password': 'password',
            'password_expiration': 'passwordExpiration',
            'permission_profile_id': 'permissionProfileId',
            'permission_profile_name': 'permissionProfileName',
            'profile_image_uri': 'profileImageUri',
            'send_activation_on_invalid_login': 'sendActivationOnInvalidLogin',
            'signature_image_uri': 'signatureImageUri',
            'suffix_name': 'suffixName',
            'title': 'title',
            'uri': 'uri',
            'user_id': 'userId',
            'user_name': 'userName',
            'user_profile_last_modified_date': 'userProfileLastModifiedDate',
            'user_settings': 'userSettings',
            'user_status': 'userStatus',
            'user_type': 'userType',
            'work_address': 'workAddress'
        }

        self._account_management_granular = account_management_granular
        self._activation_access_code = activation_access_code
        self._created_date_time = created_date_time
        self._custom_settings = custom_settings
        self._email = email
        self._enable_connect_for_user = enable_connect_for_user
        self._error_details = error_details
        self._first_name = first_name
        self._forgotten_password_info = forgotten_password_info
        self._group_list = group_list
        self._home_address = home_address
        self._initials_image_uri = initials_image_uri
        self._is_admin = is_admin
        self._last_login = last_login
        self._last_name = last_name
        self._login_status = login_status
        self._middle_name = middle_name
        self._password = password
        self._password_expiration = password_expiration
        self._permission_profile_id = permission_profile_id
        self._permission_profile_name = permission_profile_name
        self._profile_image_uri = profile_image_uri
        self._send_activation_on_invalid_login = send_activation_on_invalid_login
        self._signature_image_uri = signature_image_uri
        self._suffix_name = suffix_name
        self._title = title
        self._uri = uri
        self._user_id = user_id
        self._user_name = user_name
        self._user_profile_last_modified_date = user_profile_last_modified_date
        self._user_settings = user_settings
        self._user_status = user_status
        self._user_type = user_type
        self._work_address = work_address

    @property
    def account_management_granular(self):
        """
        Gets the account_management_granular of this UserInformation.

        :return: The account_management_granular of this UserInformation.
        :rtype: UserAccountManagementGranularInformation
        """
        return self._account_management_granular

    @account_management_granular.setter
    def account_management_granular(self, account_management_granular):
        """
        Sets the account_management_granular of this UserInformation.

        :param account_management_granular: The account_management_granular of this UserInformation.
        :type: UserAccountManagementGranularInformation
        """

        self._account_management_granular = account_management_granular

    @property
    def activation_access_code(self):
        """
        Gets the activation_access_code of this UserInformation.
        The activation code the new user must enter when activating their account.

        :return: The activation_access_code of this UserInformation.
        :rtype: str
        """
        return self._activation_access_code

    @activation_access_code.setter
    def activation_access_code(self, activation_access_code):
        """
        Sets the activation_access_code of this UserInformation.
        The activation code the new user must enter when activating their account.

        :param activation_access_code: The activation_access_code of this UserInformation.
        :type: str
        """

        self._activation_access_code = activation_access_code

    @property
    def created_date_time(self):
        """
        Gets the created_date_time of this UserInformation.
        Indicates the date and time the item was created.

        :return: The created_date_time of this UserInformation.
        :rtype: str
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """
        Sets the created_date_time of this UserInformation.
        Indicates the date and time the item was created.

        :param created_date_time: The created_date_time of this UserInformation.
        :type: str
        """

        self._created_date_time = created_date_time

    @property
    def custom_settings(self):
        """
        Gets the custom_settings of this UserInformation.
        The name/value pair information for the user custom setting.

        :return: The custom_settings of this UserInformation.
        :rtype: list[NameValue]
        """
        return self._custom_settings

    @custom_settings.setter
    def custom_settings(self, custom_settings):
        """
        Sets the custom_settings of this UserInformation.
        The name/value pair information for the user custom setting.

        :param custom_settings: The custom_settings of this UserInformation.
        :type: list[NameValue]
        """

        self._custom_settings = custom_settings

    @property
    def email(self):
        """
        Gets the email of this UserInformation.
        

        :return: The email of this UserInformation.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserInformation.
        

        :param email: The email of this UserInformation.
        :type: str
        """

        self._email = email

    @property
    def enable_connect_for_user(self):
        """
        Gets the enable_connect_for_user of this UserInformation.
        Specifies whether the user is enabled for updates from DocuSign Connect. Valid values: true or false.

        :return: The enable_connect_for_user of this UserInformation.
        :rtype: str
        """
        return self._enable_connect_for_user

    @enable_connect_for_user.setter
    def enable_connect_for_user(self, enable_connect_for_user):
        """
        Sets the enable_connect_for_user of this UserInformation.
        Specifies whether the user is enabled for updates from DocuSign Connect. Valid values: true or false.

        :param enable_connect_for_user: The enable_connect_for_user of this UserInformation.
        :type: str
        """

        self._enable_connect_for_user = enable_connect_for_user

    @property
    def error_details(self):
        """
        Gets the error_details of this UserInformation.

        :return: The error_details of this UserInformation.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this UserInformation.

        :param error_details: The error_details of this UserInformation.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def first_name(self):
        """
        Gets the first_name of this UserInformation.
        The user’s first name.  Maximum Length: 50 characters.

        :return: The first_name of this UserInformation.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserInformation.
        The user’s first name.  Maximum Length: 50 characters.

        :param first_name: The first_name of this UserInformation.
        :type: str
        """

        self._first_name = first_name

    @property
    def forgotten_password_info(self):
        """
        Gets the forgotten_password_info of this UserInformation.

        :return: The forgotten_password_info of this UserInformation.
        :rtype: ForgottenPasswordInformation
        """
        return self._forgotten_password_info

    @forgotten_password_info.setter
    def forgotten_password_info(self, forgotten_password_info):
        """
        Sets the forgotten_password_info of this UserInformation.

        :param forgotten_password_info: The forgotten_password_info of this UserInformation.
        :type: ForgottenPasswordInformation
        """

        self._forgotten_password_info = forgotten_password_info

    @property
    def group_list(self):
        """
        Gets the group_list of this UserInformation.
        A list of the group information for groups to add the user to. Group information can be found by calling [ML:GET group information]. The only required parameter is groupId.   The parameters are:  * groupId – The DocuSign group ID for the group. * groupName – The name of the group * permissionProfileId – The ID of the permission profile associated with the group. * groupType – The group type. 

        :return: The group_list of this UserInformation.
        :rtype: list[Group]
        """
        return self._group_list

    @group_list.setter
    def group_list(self, group_list):
        """
        Sets the group_list of this UserInformation.
        A list of the group information for groups to add the user to. Group information can be found by calling [ML:GET group information]. The only required parameter is groupId.   The parameters are:  * groupId – The DocuSign group ID for the group. * groupName – The name of the group * permissionProfileId – The ID of the permission profile associated with the group. * groupType – The group type. 

        :param group_list: The group_list of this UserInformation.
        :type: list[Group]
        """

        self._group_list = group_list

    @property
    def home_address(self):
        """
        Gets the home_address of this UserInformation.

        :return: The home_address of this UserInformation.
        :rtype: AddressInformationV2
        """
        return self._home_address

    @home_address.setter
    def home_address(self, home_address):
        """
        Sets the home_address of this UserInformation.

        :param home_address: The home_address of this UserInformation.
        :type: AddressInformationV2
        """

        self._home_address = home_address

    @property
    def initials_image_uri(self):
        """
        Gets the initials_image_uri of this UserInformation.
        Contains the URI for an endpoint that you can use to retrieve the initials image.

        :return: The initials_image_uri of this UserInformation.
        :rtype: str
        """
        return self._initials_image_uri

    @initials_image_uri.setter
    def initials_image_uri(self, initials_image_uri):
        """
        Sets the initials_image_uri of this UserInformation.
        Contains the URI for an endpoint that you can use to retrieve the initials image.

        :param initials_image_uri: The initials_image_uri of this UserInformation.
        :type: str
        """

        self._initials_image_uri = initials_image_uri

    @property
    def is_admin(self):
        """
        Gets the is_admin of this UserInformation.
        Determines if the feature set is actively set as part of the plan.

        :return: The is_admin of this UserInformation.
        :rtype: str
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """
        Sets the is_admin of this UserInformation.
        Determines if the feature set is actively set as part of the plan.

        :param is_admin: The is_admin of this UserInformation.
        :type: str
        """

        self._is_admin = is_admin

    @property
    def last_login(self):
        """
        Gets the last_login of this UserInformation.
        Shows the date-time when the user last logged on to the system.

        :return: The last_login of this UserInformation.
        :rtype: str
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """
        Sets the last_login of this UserInformation.
        Shows the date-time when the user last logged on to the system.

        :param last_login: The last_login of this UserInformation.
        :type: str
        """

        self._last_login = last_login

    @property
    def last_name(self):
        """
        Gets the last_name of this UserInformation.
        The user’s last name.  Maximum Length: 50 characters.

        :return: The last_name of this UserInformation.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserInformation.
        The user’s last name.  Maximum Length: 50 characters.

        :param last_name: The last_name of this UserInformation.
        :type: str
        """

        self._last_name = last_name

    @property
    def login_status(self):
        """
        Gets the login_status of this UserInformation.
        Shows the current status of the user’s password. Possible values are:   * password_reset * password_active * password_expired * password_locked * password_reset_failed  

        :return: The login_status of this UserInformation.
        :rtype: str
        """
        return self._login_status

    @login_status.setter
    def login_status(self, login_status):
        """
        Sets the login_status of this UserInformation.
        Shows the current status of the user’s password. Possible values are:   * password_reset * password_active * password_expired * password_locked * password_reset_failed  

        :param login_status: The login_status of this UserInformation.
        :type: str
        """

        self._login_status = login_status

    @property
    def middle_name(self):
        """
        Gets the middle_name of this UserInformation.
        The user’s middle name.  Maximum Length: 50 characters.

        :return: The middle_name of this UserInformation.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this UserInformation.
        The user’s middle name.  Maximum Length: 50 characters.

        :param middle_name: The middle_name of this UserInformation.
        :type: str
        """

        self._middle_name = middle_name

    @property
    def password(self):
        """
        Gets the password of this UserInformation.
        

        :return: The password of this UserInformation.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserInformation.
        

        :param password: The password of this UserInformation.
        :type: str
        """

        self._password = password

    @property
    def password_expiration(self):
        """
        Gets the password_expiration of this UserInformation.
        

        :return: The password_expiration of this UserInformation.
        :rtype: str
        """
        return self._password_expiration

    @password_expiration.setter
    def password_expiration(self, password_expiration):
        """
        Sets the password_expiration of this UserInformation.
        

        :param password_expiration: The password_expiration of this UserInformation.
        :type: str
        """

        self._password_expiration = password_expiration

    @property
    def permission_profile_id(self):
        """
        Gets the permission_profile_id of this UserInformation.
        

        :return: The permission_profile_id of this UserInformation.
        :rtype: str
        """
        return self._permission_profile_id

    @permission_profile_id.setter
    def permission_profile_id(self, permission_profile_id):
        """
        Sets the permission_profile_id of this UserInformation.
        

        :param permission_profile_id: The permission_profile_id of this UserInformation.
        :type: str
        """

        self._permission_profile_id = permission_profile_id

    @property
    def permission_profile_name(self):
        """
        Gets the permission_profile_name of this UserInformation.
        

        :return: The permission_profile_name of this UserInformation.
        :rtype: str
        """
        return self._permission_profile_name

    @permission_profile_name.setter
    def permission_profile_name(self, permission_profile_name):
        """
        Sets the permission_profile_name of this UserInformation.
        

        :param permission_profile_name: The permission_profile_name of this UserInformation.
        :type: str
        """

        self._permission_profile_name = permission_profile_name

    @property
    def profile_image_uri(self):
        """
        Gets the profile_image_uri of this UserInformation.
        

        :return: The profile_image_uri of this UserInformation.
        :rtype: str
        """
        return self._profile_image_uri

    @profile_image_uri.setter
    def profile_image_uri(self, profile_image_uri):
        """
        Sets the profile_image_uri of this UserInformation.
        

        :param profile_image_uri: The profile_image_uri of this UserInformation.
        :type: str
        """

        self._profile_image_uri = profile_image_uri

    @property
    def send_activation_on_invalid_login(self):
        """
        Gets the send_activation_on_invalid_login of this UserInformation.
        When set to **true**, specifies that an additional activation email is sent to the user if they fail a log on before activating their account. 

        :return: The send_activation_on_invalid_login of this UserInformation.
        :rtype: str
        """
        return self._send_activation_on_invalid_login

    @send_activation_on_invalid_login.setter
    def send_activation_on_invalid_login(self, send_activation_on_invalid_login):
        """
        Sets the send_activation_on_invalid_login of this UserInformation.
        When set to **true**, specifies that an additional activation email is sent to the user if they fail a log on before activating their account. 

        :param send_activation_on_invalid_login: The send_activation_on_invalid_login of this UserInformation.
        :type: str
        """

        self._send_activation_on_invalid_login = send_activation_on_invalid_login

    @property
    def signature_image_uri(self):
        """
        Gets the signature_image_uri of this UserInformation.
        Contains the URI for an endpoint that you can use to retrieve the signature image.

        :return: The signature_image_uri of this UserInformation.
        :rtype: str
        """
        return self._signature_image_uri

    @signature_image_uri.setter
    def signature_image_uri(self, signature_image_uri):
        """
        Sets the signature_image_uri of this UserInformation.
        Contains the URI for an endpoint that you can use to retrieve the signature image.

        :param signature_image_uri: The signature_image_uri of this UserInformation.
        :type: str
        """

        self._signature_image_uri = signature_image_uri

    @property
    def suffix_name(self):
        """
        Gets the suffix_name of this UserInformation.
        The suffix for the user's name.   Maximum Length: 50 characters. 

        :return: The suffix_name of this UserInformation.
        :rtype: str
        """
        return self._suffix_name

    @suffix_name.setter
    def suffix_name(self, suffix_name):
        """
        Sets the suffix_name of this UserInformation.
        The suffix for the user's name.   Maximum Length: 50 characters. 

        :param suffix_name: The suffix_name of this UserInformation.
        :type: str
        """

        self._suffix_name = suffix_name

    @property
    def title(self):
        """
        Gets the title of this UserInformation.
        The title of the user.

        :return: The title of this UserInformation.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this UserInformation.
        The title of the user.

        :param title: The title of this UserInformation.
        :type: str
        """

        self._title = title

    @property
    def uri(self):
        """
        Gets the uri of this UserInformation.
        

        :return: The uri of this UserInformation.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this UserInformation.
        

        :param uri: The uri of this UserInformation.
        :type: str
        """

        self._uri = uri

    @property
    def user_id(self):
        """
        Gets the user_id of this UserInformation.
        

        :return: The user_id of this UserInformation.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserInformation.
        

        :param user_id: The user_id of this UserInformation.
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """
        Gets the user_name of this UserInformation.
        

        :return: The user_name of this UserInformation.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this UserInformation.
        

        :param user_name: The user_name of this UserInformation.
        :type: str
        """

        self._user_name = user_name

    @property
    def user_profile_last_modified_date(self):
        """
        Gets the user_profile_last_modified_date of this UserInformation.
        

        :return: The user_profile_last_modified_date of this UserInformation.
        :rtype: str
        """
        return self._user_profile_last_modified_date

    @user_profile_last_modified_date.setter
    def user_profile_last_modified_date(self, user_profile_last_modified_date):
        """
        Sets the user_profile_last_modified_date of this UserInformation.
        

        :param user_profile_last_modified_date: The user_profile_last_modified_date of this UserInformation.
        :type: str
        """

        self._user_profile_last_modified_date = user_profile_last_modified_date

    @property
    def user_settings(self):
        """
        Gets the user_settings of this UserInformation.
         The name/value pair information for user settings. These determine the actions that a user can take in the account. The `[ML:userSettings]` are listed and described below.

        :return: The user_settings of this UserInformation.
        :rtype: list[NameValue]
        """
        return self._user_settings

    @user_settings.setter
    def user_settings(self, user_settings):
        """
        Sets the user_settings of this UserInformation.
         The name/value pair information for user settings. These determine the actions that a user can take in the account. The `[ML:userSettings]` are listed and described below.

        :param user_settings: The user_settings of this UserInformation.
        :type: list[NameValue]
        """

        self._user_settings = user_settings

    @property
    def user_status(self):
        """
        Gets the user_status of this UserInformation.
        

        :return: The user_status of this UserInformation.
        :rtype: str
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        """
        Sets the user_status of this UserInformation.
        

        :param user_status: The user_status of this UserInformation.
        :type: str
        """

        self._user_status = user_status

    @property
    def user_type(self):
        """
        Gets the user_type of this UserInformation.
        

        :return: The user_type of this UserInformation.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """
        Sets the user_type of this UserInformation.
        

        :param user_type: The user_type of this UserInformation.
        :type: str
        """

        self._user_type = user_type

    @property
    def work_address(self):
        """
        Gets the work_address of this UserInformation.

        :return: The work_address of this UserInformation.
        :rtype: AddressInformationV2
        """
        return self._work_address

    @work_address.setter
    def work_address(self, work_address):
        """
        Sets the work_address of this UserInformation.

        :param work_address: The work_address of this UserInformation.
        :type: AddressInformationV2
        """

        self._work_address = work_address

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
