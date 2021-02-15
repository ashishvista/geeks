import mysqlx

# https://dev.mysql.com/doc/dev/connector-python/8.0/tutorials/getting_started.

connection_dict = {
    'host': 'localhost',
    'port': 2000,
    'user': 'admin',
    'password': 'adminadmin@987'
}
options_dict = {}

client = mysqlx.get_client(connection_dict, options_dict)
mySession = client.get_session()

# mySession.sql("USE test").execute()
try:
    schemaList = mySession.get_schemas()

    mySession.sql("USE staging").execute()
    myResult = mySession.sql("SELECT  id,sku_id,create_date FROM staging.orderProperties as op limit 10").execute()
    rows = myResult.fetch_all()
    for row in rows:
        print(list(row))

except  Exception as e:
    print(e, "something went wrong")

finally:
    mySession.close()
    client.close()
