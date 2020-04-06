#!/usr/bin/env python3
import sys
from io import BytesIO
import pycurl
import pydig
from purl import URL
from whoisextended import *
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# parser = argparse.ArgumentParser()
# print(parser)
# parser.add_argument("-u", "--url", type=str, help="domain or subdomain website")
# args = parser.parse_args()
# print(args.url)

argument = sys.argv[1:]
logging.debug(f'Parameter : {argument}')
main_url: URL = URL(argument[0])
logging.debug(f'Main URL : {main_url}')

sub_domains = main_url.subdomains()

logging.debug(f'Subdomains : {sub_domains}')
logging.debug(f'len Subdomains:  {len(sub_domains)}')

if len(sub_domains) > 1:
    host = main_url.subdomain(len(sub_domains) - 2)
    extension = main_url.subdomain(len(sub_domains) - 1)
else:
    host = main_url.as_string().split(".")[0]
    extension = main_url.as_string().split(".")[1]

hostname = host + "." + extension

logging.debug(f'subdomain: {sub_domains}')
logging.debug(f'host: {host}')
logging.debug(f'extension: {extension}')
logging.debug(f'hostname: {hostname}')


def get_ns( host):
    return pydig.query(host, 'NS')


def get_a_record(host):
    return pydig.query(host, 'A')


def get_4a_record(host):
    return pydig.query(host, 'AAAA')


def get_curl(main_url_curl):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, main_url_curl)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.FOLLOWLOCATION, True)
    c.perform()
    logging.debug(c)

    # HTTP response code, e.g. 200.
    print('Status: %d' % c.getinfo(c.RESPONSE_CODE))
    # Elapsed time for the transfer.
    print('Time: %f' % c.getinfo(c.TOTAL_TIME))
    c.close()

    # getinfo must be called before close.
    return c


def get_whois(host, extension):
    hostname = host + "." + extension
    if extension in TLD_RE.keys():
        logging.debug(f'hostname type: {type(hostname)}')
        return whois.query(hostname)
    else:
        return hostname


def get_domain_status(whois):
    return whois.status


def get_certificates():
    pass


def get_domain_registrar(whois):
    return whois.registrar


print("NS: ", get_ns(hostname))
print("A record: ", get_a_record(hostname))
print("AAAA record: ", get_4a_record(hostname))
whoisvar = get_whois(host, extension)
print('Domain :', get_domain_registrar(whoisvar))
print('Status :', get_domain_status(whoisvar))


# print("CURL: ", get_curl(main_url.as_string()))
