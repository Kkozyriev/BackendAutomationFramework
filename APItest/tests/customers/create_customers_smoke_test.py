import pytest
import logging as logger
logger.basicConfig(level=logger.INFO)



@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("TEST: Create new customer with email and password only")
    email = ''
    password = ''

    # create payload

    # make the call

    # verify status code of the call

    # verify email in the response

    # verify customer is created in database
