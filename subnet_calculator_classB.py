"""this script for subnet calculator for class B"""

def subnet(subs):
    host_range = (256*256)//subs
    ip_b, ip_c = 0, 0
    print ("network id  -   broadcast id")
    for b in range (subs):
        if ip_c == 255: ip_b += 1; ip_c=0
        print (f"172.16.{ip_b}.{ip_c}", end=" - ")
        for ip in range(host_range):
            if ip == (host_range - 1): pass
            elif ip_c >= 255:
                ip_b += 1
                ip_c = 0
            else: ip_c += 1
        print (f"172.16.{ip_b}.{ip_c}")

if __name__=='__main__':
    sub_net_no = int(input("Enter Subnet Numbers :"))
    subnet(sub_net_no)
