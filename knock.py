#!/usr/bin/python 
import socket
import itertools
import sys
destination = "192.168.18.143"

def clean_up_ports (raw_string):
	if len(raw_string) <= 0:
		return None
	# Remove the first [
	raw_string = raw_string.replace('[','')
	# Remove the second ]
	raw_string = raw_string.replace(']','')
	#split by commas
	first_list = raw_string.split(',')
	# start e empty return list
	ports = []
	for port in first_list:
	# strip the whitespace around the string
	# and cast to a integer
		ports.append(int (port.strip()))
	return ports
def main():
	print "[+] Getting sequence"
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((destination, 1337))
	except Exception as e:
		print "[+] Unable to connect to %s on port 1337. %s" % (destination, e) 
		sys.exit(1)
	# receive the list 
	raw_list = sock.recv(20)
	# get the ports in a actual python list
	ports = clean_up_ports (raw_list)
	print "[+] Sequence is %s" % ports
	print "[+] Knocking on the door using all the possible combinations...\n"
	# Lets knock all of the possible combinations of the ports list
	for port_list in itertools.permutations (ports):
		print "[+] Knocking with sequence: %s" % (port_list,) 
	for port in port_list:
		print "[+] Knocking on port %s:%s" % (destination, port) 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		sock.settimeout(0.1)
		sock.connect_ex ((destination, port)) 
		sock.close()
	print "[+] Finished sequence knock\n"
if __name__  =='__main__':
	print "[+] Knock knock opener"
	main()
	print "[+] Done"