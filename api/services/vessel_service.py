import psycopg2.extras

def get_details(imo):
    con = psycopg2.connect(dbname="ports", user="postgres", password="",
                           host="localhost", port=5432)
    cur = con.cursor()
    query= {'imo': imo}
    qry = '''SELECT v.imo, v.vessel_type, c.name, v.vesselname from vessels v inner join company c on v.owner_id = c.id where v.imo=%(imo)s ''' % query
    cur.execute(qry)
    data = cur.fetchall()
    type = data[0][1]
    owner = data[0][2]
    name = data[0][3]
    return type, owner, name