#!/usr/bin/env python
import subprocess
import optparse
import re


def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Le nom de l'interface sur laquelle vous souhaitez modifier l'adresse MAC")
	parser.add_option("-m", "--mac", dest="new_mac", help="Nouvelle adresse MAC")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		#code to handle error
		parser.error("[-] Please specify an interface, use --help for more infos.")
	elif not options.new_mac:
		#code to handle error
		parser.error("[-] Please specify a MAC adresse, use --help for more infos.")
	return options



def change_mac(interface, new_mac):
	print("[+] Changement de l'adresse mac de " + interface + " en " + new_mac + " en cours...")
	subprocess.call(["ifconfig", interface,"down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	mac_adress_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	if mac_adress_search_result:
		return mac_adress_search_result.group(0)
	else:
		print("[-] Impossible de lire l'adresse MAC")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Adresse MAC actuelle : " + str(current_mac))
#change_mac(options.interface, options.new_mac)
