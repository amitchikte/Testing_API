from apicode.src.Utillity.dbUtility import DButilit
class DB_Customer():

    def __init__(self):
        self.db_customer = DButilit()


    def get_user_by_email(self,email):
        self.sql = f"SELECT * FROM local.wp_users  where user_email = '{email}';"
        db_rs =self.db_customer.execute_select(self.sql)
        return db_rs

    def get_random_user(self):
        self.sql = f"SELECT * FROM local.wp_users  order by rand() limit 1;"
        db_rs = self.db_customer.execute_select(self.sql)
        return db_rs









