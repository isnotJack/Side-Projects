
# Py Libs
import re
import whois
import socket
import requests
import time
import sys
# import readline
import json
from pprint import pprint
#from pycrtsh import Crtsh
from dateutil.parser import parse
from requests import get



# W3b0s1nt Banner
print("""\033[0;35m
*═════════════════════════════════════════════════════════════════════*                                                               
█  ██╗    ██╗██████╗ ██████╗  ██████╗ ███████╗ ██╗███╗   ██╗████████╗ █
█  ██║    ██║╚════██╗██╔══██╗██╔═████╗██╔════╝███║████╗  ██║╚══██╔══╝ █
█  ██║ █╗ ██║ █████╔╝██████╔╝██║██╔██║███████╗╚██║██╔██╗ ██║   ██║    █
█  ██║███╗██║ ╚═══██╗██╔══██╗████╔╝██║╚════██║ ██║██║╚██╗██║   ██║    █
█  ╚███╔███╔╝██████╔╝██████╔╝╚██████╔╝███████║ ██║██║ ╚████║   ██║    █
█   ╚══╝╚══╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝    █
█ V1.1.4                                                              █
█ W3b0s1nt: Domain Intelligence                                       █                                                         
*═════════════════════════════════════════════════════════════════════*\033[0m\033[0;32m 
  ╔═══════════════════════════════════════════════════════════════╗
  ║ Github.com/isnotJack                                          ║                                                                            
  ║ Licence:MIT                                                   ║
  ╚═══════════════════════════════════════════════════════════════╝
  \033[0m""")
time.sleep(1)

# What the script does (Sequence)
print("[1]Domain Registration Check"
      "\n[2]Get Domain IP + Data"
      "\n[3]Reverse IP Search -extract Domains with same IP (HackerTarget API)"
      "\n[4]Get DNS Records (HackerTarget API)"
      "\n[5]Whois Domain Information"
      "\n[6]Domain CERT search (CRT.SH)"
      "\n[7]Domain Reputation search WhoisXML"
      "\n[8]Subdomain scan"
      "\n[9]Historical Whois")


with open('config.json', 'r') as f:
    config = json.load(f)

WHOIS_XML_API_KEY = config['WHOIS_XML_API_KEY']
HACKERTARGET_API_KEY = config['HACKERTARGET_API_KEY']
WHOIS_FREAKS_API_KEY = config['WHOIS_FREAKS_API_KEY']

# Checking if the domain is registered
def registrationstatus(domain_name):
    """
    Checking whether the domain is registered or not
    """

    try:
        dn = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(dn.domain_name)


print("\nLet's start by checking if the domain is registered!")
query = input("\n\033[0;35m\033[1mDomain Name: \033[0m")
domain = query
print(domain, "\033[0;32m...searching for domain registration\n")
print(domain, "\033[0;32m\033[1m is registered ✅ \033[0m" if registrationstatus(
    domain) else "\033[0;31m\033[1m is not registered ❌ \033[0m")



# Main.
def main():
    registrationstatus()
    #domain_ip()
    #rev_ip()
    #rev_ip_free()
    #rev_ip_api()
    #dns_records()
    #dns_records_free()
    #dns_records_api()
    #whois_search()
    #crt_sh()
    #domain_reputation()
    #subdomain_scanner()
    #whois_history()


if __name__ == '__main__':
    main()
