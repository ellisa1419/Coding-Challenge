__author__ = "Ellisa Khoja"
import csv
import ipaddress
import helper

class Firewall:
    def __init__(self, file_path):
        self.file_path = file_path
        self.processFile(file_path)


    def processFile(self,file_path):
       self.data = {}
       self.data["inbound"] = {}
       self.data["outbound"] = {}
       self.data["inbound"]["tcp"] = [] #will contain list of tuples (port, ipaddress)
       self.data["inbound"]["udp"] = [] #will contain list of tuples
       self.data["outbound"]["tcp"] = [] #will contain list of tuples
       self.data["outbound"]["udp"] = [] #will contain list of tuples

       file = open(file_path,'r')

       reader = csv.reader(file)

       for row in reader:
           direction, protocol, port, ip_address =  row

           #convert ip address to int for easy comparison

           if '-' in ip_address: # check if its a range?
              min,max = ip_address.split('-')
              minIpRange = int(ipaddress.IPv4Address(min))
              maxIpRange = int(ipaddress.IPv4Address(max))
              ip_address = str(minIpRange) +'-' +str(maxIpRange) #convert back to string
              self.data[direction][protocol].append((port, ip_address))
           else:
               ip_address = int(ipaddress.IPv4Address(ip_address))
               self.data[direction][protocol].append((port,ip_address ))


    def accept_packet(self, direction, protocol, port, ip_address):
        valid_results = self.data[direction][protocol]

        for valid_port, valid_ip_address in valid_results:
            if helper.port_check( valid_port, port ) and helper.ip_check( valid_ip_address,ip_address ):
                return True


        return False



firewall = Firewall("input.csv")
print(firewall.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
print(firewall.accept_packet("inbound", "udp", 53, "192.168.2.1"))
print(firewall.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
print(firewall.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
print(firewall.accept_packet("inbound", "udp", 24, "52.12.48.92"))
print(firewall.accept_packet("inbound", "udp", 53, "192.168.1.1"))
print(firewall.accept_packet("inbound", "udp", 53, "192.168.2.4"))
print(firewall.accept_packet("inbound", "udp", 50, "192.168.2.4"))
print(firewall.accept_packet("outbound", "udp", 10000, "52.12.48.192"))
print(firewall.accept_packet("outbound", "udp", 1000, "52.12.48.92"))
print(firewall.accept_packet("inbound", "udp", 1, "0.0.0.0"))

