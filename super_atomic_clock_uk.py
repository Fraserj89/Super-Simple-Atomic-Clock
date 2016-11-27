# Super Atomic Clock UK
# Quick project to ask an NTP server for the time

# import modules needed (ntplib needed to be downloaded and installed)
import ntplib
from time import ctime

# Set variable of the ntplib NTP Client to call out to NTP server
ntp_server = ntplib.NTPClient()
# Set clock time response to the nequest of the NTP client to UK NTP Server
clock_time = ntp_server.request('0.uk.pool.ntp.org')

# Print time to console window
print "The Current Time/Date in the UK is: " + ctime(clock_time.tx_time)
