def ipv4_address(address):

    split_ip = address.split(".")

    if len(split_ip) != 4:
        return(False)

    #Values are between 0-255
    for i in split_ip:
        if len(i) > 1 and i[0] == '0':
            return(False)
        try:
            int_value = int(i)
            if int_value >= 0 and int_value <= 255 and i.isalnum():
                continue
            else:
                return(False)
        except:
            return(False)
    return(True)

ipv4_address('127.0.0.1\n')