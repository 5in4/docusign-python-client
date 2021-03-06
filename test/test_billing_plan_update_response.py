# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import docusign_esign
from docusign_esign.rest import ApiException
from docusign_esign.models.billing_plan_update_response import BillingPlanUpdateResponse


class TestBillingPlanUpdateResponse(unittest.TestCase):
    """ BillingPlanUpdateResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBillingPlanUpdateResponse(self):
        """
        Test BillingPlanUpdateResponse
        """
        model = docusign_esign.models.billing_plan_update_response.BillingPlanUpdateResponse()


if __name__ == '__main__':
    unittest.main()
