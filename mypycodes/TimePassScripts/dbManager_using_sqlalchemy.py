from sqlalchemy import *

db_engine = create_engine('oracle+cx_oracle://SYSADM:SYSADM@lugo.lhs-systems.com:1928/s1fsti01',echo =True)
conn = db_engine.connect()
result = conn.execute(ccontact_all.select())

print result.fetchone()