from pathlib import Path

import mysql.connector

vatsim_client_table_name = "vatsim_client_data"
vatsim_database_name = "vatsimdata"


def init_db_connection():

    # get location of script to pick up private file
    script_location = Path(__file__).absolute().parent

    # read data from untracked file
    f = open(script_location / "private.txt", "r")
    lines = f.readlines()
    print(lines)
    host = lines[0].strip()
    username = lines[1].strip()
    password = lines[2].strip()
    database = lines[3].strip()
    f.close()

    mydb = mysql.connector.connect(
        host=host,
        user=username,
        passwd=password,
        database=database
    )

    return mydb


# write to database
def write_clients_to_db(clients, mydb):

    table = vatsim_client_table_name

    vals = []

    mycursor = mydb.cursor()

    sql = "INSERT INTO {0} (update_timestamp, callsign, cid, realname, clienttype, " \
          "frequency, latitude, longitude, altitude, groundspeed, planned_aircraft, " \
          "planned_tascruise, planned_depairport, planned_altitude, planned_destairport, server, " \
          "protrevision, rating, transponder, facilitytype, visualrange, planned_revision, " \
          "planned_flighttype, planned_deptime, planned_actdeptime, planned_hrsenroute, " \
          "planned_minenroute, planned_hrsfuel, planned_minfuel, planned_altairport, planned_remarks, " \
          "planned_route, planned_depairport_lat, planned_depairport_lon, planned_destairport_lat, " \
          "planned_destairport_lon, atis_message, time_last_atis_received, time_logon, heading, " \
          "QNH_iHg, QNH_Mb) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
          "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
          "%s,%s,%s,%s,%s,%s,%s,%s)".format(table)

    # iterate through clients
    for client in clients:
        print(client)
        # obtain data per client
        vals.append(client.get_client_props_for_db())

    # write all records
    mycursor.executemany(sql, vals)

    # commit
    mydb.commit()

    # show results
    print(mycursor.rowcount, " record(s) were inserted.")
