
import os

class credentialUtility():

    def __init__(self):
        pass


    @staticmethod
    def getCredentials():
        # wc_key = os.environ.get('WC_KEY')
        wc_key = 'ck_53ff28eccaf05eb0b8a51cdd2a08fa3516d1dbca'
        # wc_secret = os.environ.get('WC_SECRET')
        wc_secret = 'cs_662e86ce92cb7ee6c6cc53bab3a73c114f454684'

        if not wc_key and not wc_secret:
            raise Exception('Please set the api keys via environmental variables')
        else:
            return {'wc_key':wc_key,'wc_secret':wc_secret}

    @staticmethod
    def get_db_Credentials():

        # db_user = os.environ.get('DB_USER')
        db_user ='root'
        # db_pass = os.environ.get('DB_PASSWORD')
        db_pass = 'root'

        if not db_user and not db_pass:
            raise Exception('Please set the api keys via environmental variables')
        else:
            return {'db_user': db_user, 'db_pass': db_pass}