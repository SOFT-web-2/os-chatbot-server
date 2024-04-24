import pymysql


class Database:
    def __init__(self, host, port, user, password):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password)

    async def query(self):
        pass

    def close(self):
        pass
