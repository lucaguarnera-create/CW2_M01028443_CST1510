import pandas as pd 

#--------migrate tables-------
def migrate_cyber_incidents_table(conn):
    path = "DATA/cyber_incidents.csv"
    df = pd.read_csv(path)
    print(df.head())
    df.to_sql('cyber_incidents', conn, if_exists='append', index=False)
    print('Data loaded successfully !')

def get_cyber_incidents(conn):
    sql = 'SELECT * FROM cyber_incidents'
    data = pd.read_sql(sql, conn)
    return data