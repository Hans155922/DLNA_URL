import socket
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import socketserver
import threading
import time
import struct
import xml.etree.ElementTree as ET
ip="192.168.6.211"
port=49152
uuid="12345678-90ab-cdef-fedc-ba0987654321"#8-4-4-4-12
NLS="12345678-90ab-cdef-fedc-ba0987654321"#我不知道什么东西，格式和uuid一样，但是不是一个东西

class SSDPServer(socketserver.UDPServer):
    allow_reuse_address = True

class SSDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        print(f"Received SSDP message:\n{data.decode('utf-8')}")

def send_ssdp_broadcast():
    ssdp_message1 = (
        "NOTIFY * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "CACHE-CONTROL: max-age=66\r\n"
        "LOCATION: http://"+ip+":"+str(port)+"/description.xml\r\n"
        "OPT: \"http://schemas.upnp.org/upnp/1/0/\"; ns=01\r\n"
        "01-NLS: "+NLS+"\r\n"
        "NT: upnp:rootdevice\r\n"
        "NTS: ssdp:alive\r\n"
        "SERVER: Linux/4.19.157-perf-download HTTP/1.0\r\n"
        "X-User-Agent: redsonic\r\n"
        "USN: uuid:"+uuid+"::upnp:rootdevice\r\n"
    )
    ssdp_message2 = (
        "NOTIFY * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "CACHE-CONTROL: max-age=66\r\n"
        "LOCATION: http://"+ip+":"+str(port)+"/description.xml\r\n"
        "OPT: \"http://schemas.upnp.org/upnp/1/0/\"; ns=01\r\n"
        "01-NLS: "+NLS+"\r\n"
        "NT: uuid:"+uuid+"\r\n"
        "NTS: ssdp:alive\r\n"
        "SERVER: Linux/4.19.157-perf-download HTTP/1.0\r\n"
        "X-User-Agent: redsonic\r\n"
        "USN: uuid:"+uuid+"\r\n"
    )
    ssdp_message3 = (
        "NOTIFY * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "CACHE-CONTROL: max-age=66\r\n"
        "LOCATION: http://"+ip+":"+str(port)+"/description.xml\r\n"
        "OPT: \"http://schemas.upnp.org/upnp/1/0/\"; ns=01\r\n"
        "01-NLS: "+NLS+"\r\n"
        "NT: urn:schemas-upnp-org:device:MediaRenderer:1\r\n"
        "NTS: ssdp:alive\r\n"
        "SERVER: Linux/4.19.157-perf-download HTTP/1.0\r\n"
        "X-User-Agent: redsonic\r\n"
        "USN: uuid:"+uuid+"::urn:schemas-upnp-org:device:MediaRenderer:1\r\n"
    )
    ssdp_message4 = (
        "NOTIFY * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "CACHE-CONTROL: max-age=66\r\n"
        "LOCATION: http://"+ip+":"+str(port)+"/description.xml\r\n"
        "OPT: \"http://schemas.upnp.org/upnp/1/0/\"; ns=01\r\n"
        "01-NLS: "+NLS+"\r\n"
        "NT: urn:schemas-upnp-org:service:AVTransport:1\r\n"
        "NTS: ssdp:alive\r\n"
        "SERVER: Linux/4.19.157-perf-download HTTP/1.0\r\n"
        "X-User-Agent: redsonic\r\n"
        "USN: uuid:"+uuid+"::urn:schemas-upnp-org:service:AVTransport:1\r\n"
    )
    ssdp_message5 = (
        "NOTIFY * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "CACHE-CONTROL: max-age=66\r\n"
        "LOCATION: http://"+ip+":"+str(port)+"/description.xml\r\n"
        "OPT: \"http://schemas.upnp.org/upnp/1/0/\"; ns=01\r\n"
        "01-NLS: "+NLS+"\r\n"
        "NT: urn:schemas-upnp-org:service:RenderingControl:1\r\n"
        "NTS: ssdp:alive\r\n"
        "SERVER: Linux/4.19.157-perf-download HTTP/1.0\r\n"
        "X-User-Agent: redsonic\r\n"
        "USN: uuid:"+uuid+"::urn:schemas-upnp-org:service:RenderingControl:1\r\n"
    )
    ssdp_message6 = (
        "NOTIFY * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "CACHE-CONTROL: max-age=66\r\n"
        "LOCATION: http://"+ip+":"+str(port)+"/description.xml\r\n"
        "OPT: \"http://schemas.upnp.org/upnp/1/0/\"; ns=01\r\n"
        "01-NLS: "+NLS+"\r\n"
        "NT: urn:schemas-upnp-org:service:ConnectionManager:1\r\n"
        "NTS: ssdp:alive\r\n"
        "SERVER: Linux/4.19.157-perf-download HTTP/1.0\r\n"
        "X-User-Agent: redsonic\r\n"
        "USN: uuid:"+uuid+"::urn:schemas-upnp-org:service:ConnectionManager:1\r\n"
    )

    multicast_group = ("239.255.255.250", 1900)
        # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, 0))  # 绑定到指定的 IP 地址
        # Set the time-to-live for the socket
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        # Send the SSDP broadcast
    sock.sendto(ssdp_message1.encode("utf-8"), multicast_group)
    sock.close()
    time.sleep(1)
        # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, 0))  # 绑定到指定的 IP 地址
        # Set the time-to-live for the socket
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        # Send the SSDP broadcast
    sock.sendto(ssdp_message2.encode("utf-8"), multicast_group)
    sock.close()
    time.sleep(1)
        # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, 0))  # 绑定到指定的 IP 地址
        # Set the time-to-live for the socket
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        # Send the SSDP broadcast
    sock.sendto(ssdp_message3.encode("utf-8"), multicast_group)
    sock.close()
    time.sleep(1)
        # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, 0))  # 绑定到指定的 IP 地址
        # Set the time-to-live for the socket
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        # Send the SSDP broadcast
    sock.sendto(ssdp_message4.encode("utf-8"), multicast_group)
    sock.close()
    time.sleep(1)
        # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, 0))  # 绑定到指定的 IP 地址
        # Set the time-to-live for the socket
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        # Send the SSDP broadcast
    sock.sendto(ssdp_message5.encode("utf-8"), multicast_group)
    sock.close()
    time.sleep(1)
        # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, 0))  # 绑定到指定的 IP 地址
        # Set the time-to-live for the socket
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        # Send the SSDP broadcast
    sock.sendto(ssdp_message6.encode("utf-8"), multicast_group)
    sock.close()
    time.sleep(1)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override the log_message method to suppress log messages
        pass
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = ET.fromstring(post_data)
        current_uri_element = data.find(".//CurrentURI")
        if current_uri_element is not None:
            current_uri_value = current_uri_element.text
            print("Current URI:", current_uri_value)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'POST request received successfully')

def start_web_server():
    handler = MyHandler
    httpd = socketserver.TCPServer(("0.0.0.0", port), handler)

    print(f"Web server is running on http://localhost:{port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

if __name__ == "__main__":
    # Start the SSDP server
    ssdp_server = SSDPServer(("0.0.0.0", 1900), SSDPHandler)
    ssdp_thread = threading.Thread(target=ssdp_server.serve_forever)
    ssdp_thread.daemon = True  # Set as daemon thread
    ssdp_thread.start()

    # Start the web server
    web_thread = threading.Thread(target=start_web_server)
    web_thread.daemon = True  # Set as daemon thread
    web_thread.start()

    try:
        while True:
            send_ssdp_broadcast()
    except KeyboardInterrupt:
        pass
    finally:
        web_thread.join()