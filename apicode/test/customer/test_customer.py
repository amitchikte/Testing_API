import pytest
import logging as logger
from apicode.src.Utillity.dbUtility import DButilit
from apicode.src.Utillity.requestUtillity import ResquestUtility
from apicode.src.dao.dao_customer import DB_Customer
from apicode.src.helper.cust_helper import customerhelper
from apicode.src.Utillity.genericutillity import random_email_and_password



@pytest.mark.tcid1
def test_create_customer_only_email_password():
    print("hii")

    logger.info("TEST:create a new customer with email and password only")
    random_info = random_email_and_password()

    email = random_info['email']
    password = random_info['password']
    logger.debug(random_info)

    # import pdb;pdb.set_trace()

    #create a payload
    payload = {'email':email ,'password':password}
    print(payload)

    # custobj = customerhelper()
    # cust = custobj.create_customer(email,password)
    # print(cust[0])
    # print(cust[1])

    custobj  = customerhelper()
    res_api = custobj.create_customer(email,password)
    # import pdb;pdb.set_trace()

   # verifying the email for response and random email passes
    assert email == res_api[1]['email'],f"Random email and actual email does not match"

    db_obj = DButilit()


    sql = f"SELECT * FROM local.wp_users  where user_email = '{email}';"

    # sql = "SELECT SELECT* FROM wp759.wpv1_users"
    rs_db = db_obj.execute_select(sql)
    #import pdb ; pdb.set_trace()

    assert rs_db[0]['ID'] == res_api[1]['id']


    # https://pypi.org/project/pytest-html/



@pytest.mark.tcid2
# VERIFY MAIL WITH DB,IS IT AVAILABLE OR NOT
def test_customer_create_same_email():
   rs_db = DB_Customer().get_random_user()
   import pdb;pdb.set_trace()
   db_email = rs_db[0]['user_email']
   payload = dict()
   payload['email'] = db_email
   payload['passowrd'] = 'password'
   rs_api = ResquestUtility().post(endpoint='customers',headers=None,expected_status=400,payload=payload)
   import pdb ; pdb.set_trace()
   assert rs_api[1]['code'] == 'registration-error-email-exists',f"Expected code message was {'registration-error-email-exists'}"
   message = f"""An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>"""
   assert len(rs_api[1]['message']) == len(message) , f"Incorrect message"

@pytest.mark.tcid3
def test_create_cust_withot_email_password():
    x = customerhelper()
    x.create_customer()

@pytest.mark.tcid4
def test_check_email_present_or_not():
    connection_of_db = DButilit()
    sql = f"SELECT * FROM local.wp_users  where user_email = 'testusersdfsznfgil@gmail.com';"
    db_rs = connection_of_db.execute_select(sql)
    # import pdb;pdb.set_trace()
    assert db_rs[0]['user_email'] == 'testusersdfsznfgil@gmail.com'

@pytest.mark.tcid5
def test_email_verified_with_db():
    create_email_password = customerhelper()
    create_cust = create_email_password.create_customer('sivareddy@123','9657363602')

    db = DButilit()
    sql = f"SELECT * FROM local.wp_users  where user_email = 'sivareddy@123';"
    db_rs = db.execute_select(sql)
    assert db_rs[0]['user_email'] == 'sivareddy@123'


