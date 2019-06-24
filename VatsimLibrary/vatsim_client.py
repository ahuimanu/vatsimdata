# a representation of a line from the vatsim-data.txt file
class VatsimClient:

    def __init__(self,
                 callsign, cid, realname, clienttype, frequency,
                 latitude, longitude, altitude, groundspeed, planned_aircraft, planned_tascruise,
                 planned_depairport, planned_altitude, planned_destairport, server, protrevision,
                 rating, transponder, facilitytype, visualrange, planned_revision, planned_flighttype, planned_deptime,
                 planned_actdeptime, planned_hrsenroute, planned_minenroute, planned_hrsfuel, planned_minfuel,
                 planned_altairport, planned_remarks, planned_route, planned_depairport_lat, planned_depairport_lon,
                 planned_destairport_lat, planned_destairport_lon, atis_message, time_last_atis_received,
                 time_logon, heading, QNH_iHg, QNH_Mb, update_timestamp
                 ):
        self.update_timestamp = update_timestamp
        self.callsign = callsign
        self.cid = cid
        self.realname = realname
        self.clienttype = clienttype
        self.frequency = frequency

        # check for null string
        if len(longitude) == 0:
            longitude = 0

        self.longitude = longitude

        if len(latitude) == 0:
            latitude = 0

        self.latitude = latitude

        if len(altitude) == 0:
            altitude = 0

        self.altitude = altitude

        if len(groundspeed) == 0:
            groundspeed = 0

        self.groundspeed = groundspeed
        self.planned_aircraft = planned_aircraft
        self.planned_tascruise = planned_tascruise
        self.planned_depairport = planned_depairport
        self.planned_altitude = planned_altitude
        self.planned_destairport = planned_destairport
        self.server = server
        self.protrevision = protrevision
        self.rating = rating
        self.transponder = transponder
        self.facilitytype = facilitytype
        self.visualrange = visualrange
        self.planned_revision = planned_revision
        self.planned_flighttype = planned_revision
        self.planned_deptime = planned_deptime
        self.planned_actdeptime = planned_actdeptime
        self.planned_hrsenroute = planned_hrsenroute
        self.planned_minenroute = planned_minenroute
        self.planned_hrsfuel = planned_hrsfuel
        self.planned_minfuel = planned_minfuel
        self.planned_altairport = planned_altairport
        self.planned_remarks = planned_remarks
        self.planned_route = planned_route
        self.planned_depairport_lat = planned_depairport_lat
        self.planned_depairport_lon = planned_destairport_lon
        self.planned_destairport_lat = planned_destairport_lat
        self.planned_destairport_lon = planned_destairport_lon
        self.atis_message = atis_message
        self.time_last_atis_received = time_last_atis_received
        self.time_logon = time_logon
        self.heading = heading
        self.QNH_iHg = QNH_iHg
        self.QNH_Mb = QNH_Mb

    def __str__(self):
        return \
            "[VATSIM CLIENT]" \
            "[TIMESTAMP] {0}|" \
            "callsign: {1}|" \
            "cid: {2}|" \
            "Name: {3}|" \
            "Type: {4}|" \
            "Server: {5}-{6}|" \
            "[PILOT]" \
            "{7}|" \
            "{8}|" \
            "{9}|" \
            "{10}|" \
            "{11}|" \
            "{12}|" \
            "{13}|" \
            "{14}|" \
            "{15}|" \
            "{16}|" \
            "{17}-{18}|" \
            "{19}|" \
            "{20}|" \
            "{21}-{22}|" \
            "{23}|" \
            "{24}|" \
            "{25}|" \
            "{26}|" \
            "{27}|" \
            "{28}|" \
            "{29}|" \
            "{30}|" \
            "{31}|" \
            "ALT {32}|" \
            "ROUTE {33}|" \
            "RMK {34}|" \
            "ATC" \
            "{35}|" \
            "FREQ {36}|" \
            "type {37}|" \
            "{38}|" \
            "{39}|" \
            "{40}|" \
            "{41}|".format(self.update_timestamp,
                           self.callsign,
                           self.cid,
                           self.realname,
                           self.clienttype,
                           self.server,
                           self.protrevision,
                           self.latitude,
                           self.longitude,
                           self.altitude,
                           self.groundspeed,
                           self.heading,
                           self.QNH_iHg,
                           self.QNH_Mb,
                           self.transponder,
                           self.planned_aircraft,
                           self.planned_tascruise,
                           self.planned_depairport,
                           self.planned_depairport_lat,
                           self.planned_depairport_lon,
                           self.planned_altitude,
                           self.planned_destairport,
                           self.planned_destairport_lat,
                           self.planned_destairport_lon,
                           self.planned_revision,
                           self.planned_flighttype,
                           self.planned_deptime,
                           self.planned_actdeptime,
                           self.planned_hrsenroute,
                           self.planned_minenroute,
                           self.planned_hrsfuel,
                           self.planned_minfuel,
                           self.planned_altairport,
                           self.planned_route,
                           self.planned_remarks,
                           self.rating,
                           self.frequency,
                           self.facilitytype,
                           self.visualrange,
                           self.atis_message,
                           self.time_last_atis_received,
                           self.time_logon)

    def get_client_props_for_db(self):

        val = (self.update_timestamp, self.callsign, self.cid, self.realname, self.clienttype, self.frequency,
               self.latitude, self.longitude, self.altitude, self.groundspeed, self.planned_aircraft,
               self.planned_tascruise, self.planned_destairport, self.planned_altitude,self.planned_destairport,
               self.server, self.protrevision, self.rating, self.transponder, self.facilitytype, self.visualrange,
               self.planned_revision, self.planned_flighttype, self.planned_deptime, self.planned_actdeptime,
               self.planned_hrsenroute, self.planned_minenroute, self.planned_hrsfuel, self.planned_minfuel,
               self.planned_altairport, self.planned_remarks, self.planned_route, self.planned_depairport_lat,
               self.planned_depairport_lon, self.planned_destairport_lat, self.planned_destairport_lon,
               self.atis_message, self.time_last_atis_received, self.time_logon, self.heading, self.QNH_iHg,
               self.QNH_Mb)

        return val

