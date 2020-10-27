import socket
import dns.resolver

hostname = str(input("Website: "))

Ipaddress = socket.gethostbyname(hostname)

print("IP address: ")
print(Ipaddress)

try:
    result = dns.resolver.resolve(hostname, 'CNAME')
    for cnameval in result:
        print(" cname target address:", cnameval.target)
except dns.resolver.NoAnswer:
    print("no CNAME")



