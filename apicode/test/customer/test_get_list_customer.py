import pytest
from apicode.src.Utillity.requestUtillity import ResquestUtility

@pytest.mark.customer
@pytest.mark.tcid6
def test_get_customers():

    # make a call to get all customers
    r = ResquestUtility()
    rs_api =  r.get(endpoint='customers',headers=None,expected_status=200)
    # verify whether the responce is not empty
    assert rs_api ,f"No customer is present"
    #import pdb ; pdb.set_trace()
    # validate response is not empty