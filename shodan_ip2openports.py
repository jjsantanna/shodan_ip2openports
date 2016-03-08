import sys
import shodan

SHODAN_API_KEY = "" #your personal Shodan key 

api = shodan.Shodan(SHODAN_API_KEY)

if len(sys.argv) == 1:
        print 'Usage: %s <IP_address>' % sys.argv[0]
        sys.exit(1)

input_ip = ' '.join(sys.argv[1:])

try:
	host_info = api.host(input_ip)
 
	# Getting the open ports
	open_ports=""
	for item in host_info['data']:
		open_ports += str(item['port'])+"," # Concatenating all the open ports (after convert int to string)

	# FINISHING BY Printing (i) the input_ip IP Address, (ii) last checked by Shodan, and (iii) the open ports
	print host_info['ip_str']+";"+host_info['last_update']+";"+open_ports[:-1]

except:
	print input_ip+";Not_Found" 
