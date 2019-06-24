# VATSIMLIB

import os
import random
import requests

from datetime import datetime
from pathlib import Path
from VatsimLibrary.vatsim_client import VatsimClient

# CONSTANTS
DATA_SERVER_PREFIX = "url0"
FIELD_DELIMITER = ":"
METAR_SERVER_PREFIX = "metar0"
STATUS_URL = "http://status.vatsim.net/"

# store current data urls
data_urls_list = []

# store metar URL
selected_metar_url = ""

# store selected data URL
selected_data_url = ""

# vatsim datafile update timestamp string (not a python datetime object)
vatsim_data_file_update_timestamp = ""

# script location in filesystem
script_location = Path(__file__).absolute().parent
status_temp_file = script_location / 'status.txt'
vatsim_data_file = script_location / 'vatsim-data.txt'


# read metar information from VATSIM
def get_metar_report_by_id(metar_id):

    global selected_metar_url
    handle = None

    # find status file to read metar URL
    if os.path.exists(status_temp_file):
        handle = open(status_temp_file, "r+")

    # look for metar url prefix
    with handle as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            if line.startswith(METAR_SERVER_PREFIX):
                # no need to use the whole line, just use the url
                selected_metar_url = line[7:]
                # remove any whitespace and other weirdness
                selected_metar_url = selected_metar_url.strip()
                print(selected_metar_url)

    if selected_metar_url:
        result = requests.get(selected_metar_url + "?id=" + metar_id)
        result.raise_for_status()

        print(result.text)


# randomly obtain one of the provided data URLs
def get_random_data_server():

    global selected_data_url
    handle = None

    if not os.path.exists(status_temp_file):
        handle = open(status_temp_file, "w")
    else:
        handle = open(status_temp_file, "r+")

    with handle as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            if line.startswith(DATA_SERVER_PREFIX):
                data_urls_list.append(line)

    if len(data_urls_list) > 0:
        selected_data_url = data_urls_list[random.randint(0, len(data_urls_list) - 1)]

        # remove extra characters
        selected_data_url = selected_data_url.strip()

        # list slicing
        selected_data_url = selected_data_url[5:]
    else:
        selected_data_url = ""

    return selected_data_url


# check to see if the status file should be downloaded
def status_file_is_stale():
    handle = None

    if os.path.exists(status_temp_file):
        lastmodified = os.stat('file.txt').st_mtime
        timestamplast = datetime.fromtimestamp(lastmodified)
        timestampnow = datetime.utcnow()
        diff = timestampnow - timestamplast

        if diff.seconds / (60 * 60) > 24:
            print("STALE! Hours: {0}".format(diff.seconds / (60 * 60)))
            return False

        else:
            print("FRESH! Hours: {0}".format(diff.seconds / (60 * 60)))
            return True

    else:
        return True


# parse the status file to pick up the correct URLs to use
def get_status_file(url):

    # get file from VATSIM
    result = requests.get(url)
    result.raise_for_status()

    # file handle
    handle = None

    if not os.path.exists(status_temp_file) or status_file_is_stale():
        handle = open(status_temp_file, "w")
        handle.write(result.text)
        handle.close()


# write out a temporary file and use that for further processing
def write_vatsim_datafile(url):

    result = requests.get(url)
    result.raise_for_status()

    # dispose of the previous file
    if os.path.exists(vatsim_data_file):
        print('exist')
        os.remove(vatsim_data_file)

    handle = None
    # handle = open(vatsim_data_file, "w", encoding="utf8")
    handle = open(vatsim_data_file, "w+b")
    handle.write(result.text.encode('utf8'))
    # handle.write(result.text)
    print("vatsim-data written")
    handle.close()


# parse a line from the client file for input
def parse_vatsim_client(line):

    # filter for any extraneous information - don't start with these characters
    if line.startswith("!") or line.startswith(";") or line.startswith(" "):
        return

    # break up the string into its parts on the delimiter
    parts = line.split(FIELD_DELIMITER)

    client = VatsimClient(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5],
                          parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12], parts[13], parts[14],
                          parts[15], parts[16], parts[17], parts[18], parts[19], parts[20], parts[21], parts[22],
                          parts[23], parts[24], parts[25], parts[26], parts[27], parts[28], parts[29], parts[30],
                          parts[31], parts[32], parts[33], parts[34], parts[35], parts[36], parts[37], parts[38],
                          parts[39], parts[40], vatsim_data_file_update_timestamp)

    # print(client)
    return client


# isolate just the clients in the range
def extract_client_range():

    # store current client objects list
    current_clients = []

    global vatsim_data_file_update_timestamp
    client_range_start = 0
    client_range_end = 0
    handle = None

    if os.path.exists(vatsim_data_file):
        print("file exists in extract client range")
        handle = open(vatsim_data_file, "r+")
    else:
        pass

    lines = handle.readlines()

    # find the beginning of client range
    for i in range(len(lines)):

        if lines[i].startswith("UPDATE ="):
            vatsim_data_file_update_timestamp = lines[i][9:]
            print("VATSIM UPDATE TIME: {0}".format(vatsim_data_file_update_timestamp))

        if lines[i].startswith("!CLIENTS:"):
            client_range_start = i + 1

        if lines[i].startswith("!SERVERS"):
            client_range_end = i - 2

    print("start: {0} end: {1}".format(client_range_start, client_range_end))

    for z in range(client_range_start, client_range_end):
        # store current client objects list
        current_clients.append(parse_vatsim_client(lines[z]))

    return current_clients

