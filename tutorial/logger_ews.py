import re
import urllib3
from exchangelib import DELEGATE, Account, Credentials, Configuration
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import socket

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

username = "soar"
password = "exide@1234"
server = "mail.in.intranet"
email = "soar@exidelife.in"

ews_url = "https://mail.in.intranet/ews/exchange.asmx"
UDP_HOST = "10.10.10.112"
UDP_PORT = 5142
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

creds = Credentials(username=username, password=password)

config = Configuration(service_endpoint=ews_url, credentials=creds)
account = Account(
    primary_smtp_address=email,
    credentials=creds,
    config=config,
    autodiscover=False,
    access_type=DELEGATE)

for item in account.inbox.all().order_by('-datetime_received')[:5]:
    # print(item.body)
    body = item.body
    body_string = re.sub(r"\s+", " ", body)
    print(body_string)
    # stream_log = bytearray(body_string.encode())
    # clientSock.sendto(stream_log, (UDP_HOST, int(UDP_PORT)))
