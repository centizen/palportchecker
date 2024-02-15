import socket

def sendpacket(payload, server_address, server_port):
    try:
        server_ip = socket.gethostbyname(server_address)
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.settimeout(5.0) 
        packet = bytes(payload)
        udp_socket.sendto(packet, (server_ip, server_port))
        response, addr = udp_socket.recvfrom(1024)
        return response

    except socket.timeout:
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        udp_socket.close()

server_domain = input("Type or Paste your External IP Address or Hostname\t")
server_port = int(input("Type or Paste your servers port (Default: 8211):\t"))
magic_bytes = [0x09, 0x08, 0x00, 0x08, 0xb4, 0xb5, 0x09, 0xb2,
                  0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0xb8, 0xc0, 0xbb, 0x35,
                  0x47, 0x50, 0xf3, 0xed, 0x49, 0x62, 0xa2, 0x9e,
                  0x39, 0xab, 0x0b]  

response = sendpacket(magic_bytes, server_domain, server_port)

if response:
    print("#######################################################")
    print("##  SUCCESS: Port is open and server is responding!  ##")
    print("##         Players should be able to connect.        ##")
    print("#######################################################")
else:
    print("############################################################")
    print("##  ERROR: Did not receive a response from your server.   ##")
    print("##  Check your settings and make sure the server is on!   ##")
    print("############################################################")
