from app.db import conn
from app.cyber_incidents import get_cyber_incidents, migrate_cyber_incidents_table

migrate_cyber_incidents_table(conn)
data = get_cyber_incidents(conn)
print(data.head())