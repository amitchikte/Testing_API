
import requests
import json
import logging as logger
import os
from apicode.src.config.hostconfig import API_HOST
from requests_oauthlib import OAuth1

# import os
from apicode.src.Utillity.credentialsUtilities import credentialUtility


class ResquestUtility(object):

    def __init__(self):
        self.baseurl = "http://amit.local/wp-json/wc/v3/"
        wc_credentials = credentialUtility().getCredentials()
        self.env = os.environ.get('ENV', "test")
        self.baseurl = API_HOST[self.env]
        self.auth = OAuth1(wc_credentials['wc_key'], wc_credentials['wc_secret'])


    def assert_status_code(self):
        assert self.status_code == self.expected_status,f"bad status code"

    def post(self,endpoint,payload,headers = None,expected_status = 200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.baseurl + endpoint
        rs_api = requests.post(url=self.url,data= json.dumps(payload),headers=headers,auth = self.auth)
        logger.info(rs_api.json())
        self.status_code = rs_api.status_code
        self.expected_status = expected_status
        self.rs_json = rs_api.json()
        logger.debug(f"The post request response is{self.rs_json}")
        return [self.status_code,self.rs_json]

    def get(self,endpoint,headers = None,expected_status = 200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.baseurl + endpoint
        rs_api = requests.get(url = self.url,headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status = expected_status
        self.rs_json = rs_api.json()
        logger.debug(f"The get request response is{self.rs_json}")
        return [self.status_code,self.rs_json]


