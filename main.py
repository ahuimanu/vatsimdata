from VatsimLibrary.vatsimlib import extract_client_range, \
                                    get_random_data_server, \
                                    get_status_file, \
                                    STATUS_URL, \
                                    write_vatsim_datafile, \
                                    get_metar_report_by_id

from VatsimLibrary.vatsimlib_dbinfo import init_db_connection, \
                                           write_clients_to_db

print("RETRIEVE DATA")

# get latest servers
get_status_file(STATUS_URL)

# get metar for KAMA
get_metar_report_by_id("KAMA")

# obtain random url, read vatsim data and store in file
url = get_random_data_server()
write_vatsim_datafile(get_random_data_server())

# extract clients
clients = extract_client_range()

print("INIT DATABASE...")
mydb = init_db_connection()

print("WRITE TO DATABASE...")
# write to db
write_clients_to_db(clients, mydb)

