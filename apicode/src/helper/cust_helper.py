from apicode.src.Utillity.genericutillity import random_email_and_password
from apicode.src.Utillity.requestUtillity import ResquestUtility

class customerhelper(object):
    def __init__(self):
        self.request_utility = ResquestUtility()

    def create_customer(self,email=None,password=None):
        if not email:
            email = random_email_and_password()["email"]
        if not password:
            password = random_email_and_password()["password"]

        payload = dict()
        payload["email"] = email
        payload["password"] = password

        rs_api = self.request_utility.post('customers',payload,expected_status=201,headers=None)
        # rs_api = self.request_utility.get("api/users?page=2",expected_status=200,headers=None)


        return rs_api