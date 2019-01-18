__author__ = "Ellisa Khoja"
import ipaddress

def port_check(valid_port,port):
        port = str(port)
        if '-' in valid_port: #is it a range?
            min, max = valid_port.split('-')
            return min <= port  <= max

        else:
            return valid_port == port


def ip_check(valid_ip_address,ip_address):
        ip_address = int(ipaddress.IPv4Address(ip_address))

        if '-' in str(valid_ip_address): #is it a range?
            min, max = valid_ip_address.split('-')
            return int(min) <= ip_address <= int(max)

        else:
            return valid_ip_address == ip_address

