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


class AccountBillingPlan(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, add_ons=None, can_cancel_renewal=None, can_upgrade=None, currency_code=None, enable_support=None, included_seats=None, incremental_seats=None, is_downgrade=None, other_discount_percent=None, payment_cycle=None, payment_method=None, per_seat_price=None, plan_classification=None, plan_feature_sets=None, plan_id=None, plan_name=None, renewal_status=None, seat_discounts=None, support_incident_fee=None, support_plan_fee=None):
        """
        AccountBillingPlan - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'add_ons': 'list[AddOn]',
            'can_cancel_renewal': 'str',
            'can_upgrade': 'str',
            'currency_code': 'str',
            'enable_support': 'str',
            'included_seats': 'str',
            'incremental_seats': 'str',
            'is_downgrade': 'str',
            'other_discount_percent': 'str',
            'payment_cycle': 'str',
            'payment_method': 'str',
            'per_seat_price': 'str',
            'plan_classification': 'str',
            'plan_feature_sets': 'list[FeatureSet]',
            'plan_id': 'str',
            'plan_name': 'str',
            'renewal_status': 'str',
            'seat_discounts': 'list[SeatDiscount]',
            'support_incident_fee': 'str',
            'support_plan_fee': 'str'
        }

        self.attribute_map = {
            'add_ons': 'addOns',
            'can_cancel_renewal': 'canCancelRenewal',
            'can_upgrade': 'canUpgrade',
            'currency_code': 'currencyCode',
            'enable_support': 'enableSupport',
            'included_seats': 'includedSeats',
            'incremental_seats': 'incrementalSeats',
            'is_downgrade': 'isDowngrade',
            'other_discount_percent': 'otherDiscountPercent',
            'payment_cycle': 'paymentCycle',
            'payment_method': 'paymentMethod',
            'per_seat_price': 'perSeatPrice',
            'plan_classification': 'planClassification',
            'plan_feature_sets': 'planFeatureSets',
            'plan_id': 'planId',
            'plan_name': 'planName',
            'renewal_status': 'renewalStatus',
            'seat_discounts': 'seatDiscounts',
            'support_incident_fee': 'supportIncidentFee',
            'support_plan_fee': 'supportPlanFee'
        }

        self._add_ons = add_ons
        self._can_cancel_renewal = can_cancel_renewal
        self._can_upgrade = can_upgrade
        self._currency_code = currency_code
        self._enable_support = enable_support
        self._included_seats = included_seats
        self._incremental_seats = incremental_seats
        self._is_downgrade = is_downgrade
        self._other_discount_percent = other_discount_percent
        self._payment_cycle = payment_cycle
        self._payment_method = payment_method
        self._per_seat_price = per_seat_price
        self._plan_classification = plan_classification
        self._plan_feature_sets = plan_feature_sets
        self._plan_id = plan_id
        self._plan_name = plan_name
        self._renewal_status = renewal_status
        self._seat_discounts = seat_discounts
        self._support_incident_fee = support_incident_fee
        self._support_plan_fee = support_plan_fee

    @property
    def add_ons(self):
        """
        Gets the add_ons of this AccountBillingPlan.
        Reserved:

        :return: The add_ons of this AccountBillingPlan.
        :rtype: list[AddOn]
        """
        return self._add_ons

    @add_ons.setter
    def add_ons(self, add_ons):
        """
        Sets the add_ons of this AccountBillingPlan.
        Reserved:

        :param add_ons: The add_ons of this AccountBillingPlan.
        :type: list[AddOn]
        """

        self._add_ons = add_ons

    @property
    def can_cancel_renewal(self):
        """
        Gets the can_cancel_renewal of this AccountBillingPlan.
        Reserved: TBD

        :return: The can_cancel_renewal of this AccountBillingPlan.
        :rtype: str
        """
        return self._can_cancel_renewal

    @can_cancel_renewal.setter
    def can_cancel_renewal(self, can_cancel_renewal):
        """
        Sets the can_cancel_renewal of this AccountBillingPlan.
        Reserved: TBD

        :param can_cancel_renewal: The can_cancel_renewal of this AccountBillingPlan.
        :type: str
        """

        self._can_cancel_renewal = can_cancel_renewal

    @property
    def can_upgrade(self):
        """
        Gets the can_upgrade of this AccountBillingPlan.
        When set to **true**, specifies that you can upgrade the account through the API.

        :return: The can_upgrade of this AccountBillingPlan.
        :rtype: str
        """
        return self._can_upgrade

    @can_upgrade.setter
    def can_upgrade(self, can_upgrade):
        """
        Sets the can_upgrade of this AccountBillingPlan.
        When set to **true**, specifies that you can upgrade the account through the API.

        :param can_upgrade: The can_upgrade of this AccountBillingPlan.
        :type: str
        """

        self._can_upgrade = can_upgrade

    @property
    def currency_code(self):
        """
        Gets the currency_code of this AccountBillingPlan.
        Specifies the ISO currency code for the account.

        :return: The currency_code of this AccountBillingPlan.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this AccountBillingPlan.
        Specifies the ISO currency code for the account.

        :param currency_code: The currency_code of this AccountBillingPlan.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def enable_support(self):
        """
        Gets the enable_support of this AccountBillingPlan.
        When set to **true**, then customer support is provided as part of the account plan.

        :return: The enable_support of this AccountBillingPlan.
        :rtype: str
        """
        return self._enable_support

    @enable_support.setter
    def enable_support(self, enable_support):
        """
        Sets the enable_support of this AccountBillingPlan.
        When set to **true**, then customer support is provided as part of the account plan.

        :param enable_support: The enable_support of this AccountBillingPlan.
        :type: str
        """

        self._enable_support = enable_support

    @property
    def included_seats(self):
        """
        Gets the included_seats of this AccountBillingPlan.
        The number of seats (users) included.

        :return: The included_seats of this AccountBillingPlan.
        :rtype: str
        """
        return self._included_seats

    @included_seats.setter
    def included_seats(self, included_seats):
        """
        Sets the included_seats of this AccountBillingPlan.
        The number of seats (users) included.

        :param included_seats: The included_seats of this AccountBillingPlan.
        :type: str
        """

        self._included_seats = included_seats

    @property
    def incremental_seats(self):
        """
        Gets the incremental_seats of this AccountBillingPlan.
        Reserved: TBD

        :return: The incremental_seats of this AccountBillingPlan.
        :rtype: str
        """
        return self._incremental_seats

    @incremental_seats.setter
    def incremental_seats(self, incremental_seats):
        """
        Sets the incremental_seats of this AccountBillingPlan.
        Reserved: TBD

        :param incremental_seats: The incremental_seats of this AccountBillingPlan.
        :type: str
        """

        self._incremental_seats = incremental_seats

    @property
    def is_downgrade(self):
        """
        Gets the is_downgrade of this AccountBillingPlan.
        

        :return: The is_downgrade of this AccountBillingPlan.
        :rtype: str
        """
        return self._is_downgrade

    @is_downgrade.setter
    def is_downgrade(self, is_downgrade):
        """
        Sets the is_downgrade of this AccountBillingPlan.
        

        :param is_downgrade: The is_downgrade of this AccountBillingPlan.
        :type: str
        """

        self._is_downgrade = is_downgrade

    @property
    def other_discount_percent(self):
        """
        Gets the other_discount_percent of this AccountBillingPlan.
         Any other percentage discount for the plan. 

        :return: The other_discount_percent of this AccountBillingPlan.
        :rtype: str
        """
        return self._other_discount_percent

    @other_discount_percent.setter
    def other_discount_percent(self, other_discount_percent):
        """
        Sets the other_discount_percent of this AccountBillingPlan.
         Any other percentage discount for the plan. 

        :param other_discount_percent: The other_discount_percent of this AccountBillingPlan.
        :type: str
        """

        self._other_discount_percent = other_discount_percent

    @property
    def payment_cycle(self):
        """
        Gets the payment_cycle of this AccountBillingPlan.
        

        :return: The payment_cycle of this AccountBillingPlan.
        :rtype: str
        """
        return self._payment_cycle

    @payment_cycle.setter
    def payment_cycle(self, payment_cycle):
        """
        Sets the payment_cycle of this AccountBillingPlan.
        

        :param payment_cycle: The payment_cycle of this AccountBillingPlan.
        :type: str
        """

        self._payment_cycle = payment_cycle

    @property
    def payment_method(self):
        """
        Gets the payment_method of this AccountBillingPlan.
         The payment method used with the plan. The possible values are: CreditCard, PurchaseOrder, Premium, or Freemium. 

        :return: The payment_method of this AccountBillingPlan.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this AccountBillingPlan.
         The payment method used with the plan. The possible values are: CreditCard, PurchaseOrder, Premium, or Freemium. 

        :param payment_method: The payment_method of this AccountBillingPlan.
        :type: str
        """

        self._payment_method = payment_method

    @property
    def per_seat_price(self):
        """
        Gets the per_seat_price of this AccountBillingPlan.
        

        :return: The per_seat_price of this AccountBillingPlan.
        :rtype: str
        """
        return self._per_seat_price

    @per_seat_price.setter
    def per_seat_price(self, per_seat_price):
        """
        Sets the per_seat_price of this AccountBillingPlan.
        

        :param per_seat_price: The per_seat_price of this AccountBillingPlan.
        :type: str
        """

        self._per_seat_price = per_seat_price

    @property
    def plan_classification(self):
        """
        Gets the plan_classification of this AccountBillingPlan.
        Identifies the type of plan. Examples include Business, Corporate, Enterprise, Free.

        :return: The plan_classification of this AccountBillingPlan.
        :rtype: str
        """
        return self._plan_classification

    @plan_classification.setter
    def plan_classification(self, plan_classification):
        """
        Sets the plan_classification of this AccountBillingPlan.
        Identifies the type of plan. Examples include Business, Corporate, Enterprise, Free.

        :param plan_classification: The plan_classification of this AccountBillingPlan.
        :type: str
        """

        self._plan_classification = plan_classification

    @property
    def plan_feature_sets(self):
        """
        Gets the plan_feature_sets of this AccountBillingPlan.
        A complex type that sets the feature sets for the account. It contains the following information (all string content):  * currencyFeatureSetPrices - Contains the currencyCode and currencySymbol for the alternate currency values for envelopeFee, fixedFee, seatFee that are configured for this plan feature set. * envelopeFee - An incremental envelope cost for plans with envelope overages (when isEnabled=true). * featureSetId - A unique ID for the feature set. * fixedFee - A one-time fee associated with the plan (when isEnabled=true). * isActive - Specifies whether the feature set is actively set as part of the plan. * isEnabled - Specifies whether the feature set is actively enabled as part of the plan. * name - The name of the feature set. * seatFee - An incremental seat cost for seat-based plans (when isEnabled=true). 

        :return: The plan_feature_sets of this AccountBillingPlan.
        :rtype: list[FeatureSet]
        """
        return self._plan_feature_sets

    @plan_feature_sets.setter
    def plan_feature_sets(self, plan_feature_sets):
        """
        Sets the plan_feature_sets of this AccountBillingPlan.
        A complex type that sets the feature sets for the account. It contains the following information (all string content):  * currencyFeatureSetPrices - Contains the currencyCode and currencySymbol for the alternate currency values for envelopeFee, fixedFee, seatFee that are configured for this plan feature set. * envelopeFee - An incremental envelope cost for plans with envelope overages (when isEnabled=true). * featureSetId - A unique ID for the feature set. * fixedFee - A one-time fee associated with the plan (when isEnabled=true). * isActive - Specifies whether the feature set is actively set as part of the plan. * isEnabled - Specifies whether the feature set is actively enabled as part of the plan. * name - The name of the feature set. * seatFee - An incremental seat cost for seat-based plans (when isEnabled=true). 

        :param plan_feature_sets: The plan_feature_sets of this AccountBillingPlan.
        :type: list[FeatureSet]
        """

        self._plan_feature_sets = plan_feature_sets

    @property
    def plan_id(self):
        """
        Gets the plan_id of this AccountBillingPlan.
        

        :return: The plan_id of this AccountBillingPlan.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this AccountBillingPlan.
        

        :param plan_id: The plan_id of this AccountBillingPlan.
        :type: str
        """

        self._plan_id = plan_id

    @property
    def plan_name(self):
        """
        Gets the plan_name of this AccountBillingPlan.
        The name of the Billing Plan.

        :return: The plan_name of this AccountBillingPlan.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """
        Sets the plan_name of this AccountBillingPlan.
        The name of the Billing Plan.

        :param plan_name: The plan_name of this AccountBillingPlan.
        :type: str
        """

        self._plan_name = plan_name

    @property
    def renewal_status(self):
        """
        Gets the renewal_status of this AccountBillingPlan.
        The renewal status for the account. The acceptable values are:  * auto: The account automatically renews. * queued_for_close: Account will be closed at the billingPeriodEndDate. * queued_for_downgrade: Account will be downgraded at the billingPeriodEndDate.

        :return: The renewal_status of this AccountBillingPlan.
        :rtype: str
        """
        return self._renewal_status

    @renewal_status.setter
    def renewal_status(self, renewal_status):
        """
        Sets the renewal_status of this AccountBillingPlan.
        The renewal status for the account. The acceptable values are:  * auto: The account automatically renews. * queued_for_close: Account will be closed at the billingPeriodEndDate. * queued_for_downgrade: Account will be downgraded at the billingPeriodEndDate.

        :param renewal_status: The renewal_status of this AccountBillingPlan.
        :type: str
        """

        self._renewal_status = renewal_status

    @property
    def seat_discounts(self):
        """
        Gets the seat_discounts of this AccountBillingPlan.
         A complex type that contains any seat discount information.  Values are: BeginSeatCount, EndSeatCount, and SeatDiscountPercent.  

        :return: The seat_discounts of this AccountBillingPlan.
        :rtype: list[SeatDiscount]
        """
        return self._seat_discounts

    @seat_discounts.setter
    def seat_discounts(self, seat_discounts):
        """
        Sets the seat_discounts of this AccountBillingPlan.
         A complex type that contains any seat discount information.  Values are: BeginSeatCount, EndSeatCount, and SeatDiscountPercent.  

        :param seat_discounts: The seat_discounts of this AccountBillingPlan.
        :type: list[SeatDiscount]
        """

        self._seat_discounts = seat_discounts

    @property
    def support_incident_fee(self):
        """
        Gets the support_incident_fee of this AccountBillingPlan.
        The support incident fee charged for each support incident.

        :return: The support_incident_fee of this AccountBillingPlan.
        :rtype: str
        """
        return self._support_incident_fee

    @support_incident_fee.setter
    def support_incident_fee(self, support_incident_fee):
        """
        Sets the support_incident_fee of this AccountBillingPlan.
        The support incident fee charged for each support incident.

        :param support_incident_fee: The support_incident_fee of this AccountBillingPlan.
        :type: str
        """

        self._support_incident_fee = support_incident_fee

    @property
    def support_plan_fee(self):
        """
        Gets the support_plan_fee of this AccountBillingPlan.
        The support plan fee charged for this plan.

        :return: The support_plan_fee of this AccountBillingPlan.
        :rtype: str
        """
        return self._support_plan_fee

    @support_plan_fee.setter
    def support_plan_fee(self, support_plan_fee):
        """
        Sets the support_plan_fee of this AccountBillingPlan.
        The support plan fee charged for this plan.

        :param support_plan_fee: The support_plan_fee of this AccountBillingPlan.
        :type: str
        """

        self._support_plan_fee = support_plan_fee

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
