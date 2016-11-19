import re

def ipv4_address(address):
    
    split_ip = address.split()

    if len(split_ip) < 4:
        print("Fail")
    #Check for leading Zeroes

    #Values are between 0-255


ipv4_address('127.0.0.1')