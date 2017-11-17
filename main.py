mport socket
import struct

class request_query:
    def __init__(self):
        self.transaction_id = 0
        self.flags = 0
        self.question_count = 0
        self.answer_count = 0
        self.name_service_cout = 0
        self.additional_record_count = 0
        self.question_name = ""
        self.question_type = 0
        self.question_class = 0


def main():

    ip_port = ('224.0.0.251', 137)
    bind_ip = ('192.168.193.52', 64335)
    udp = socket.getprotobyname("udp")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,udp)

    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(bind_ip)

    buf = request_query()

    buf.question_class = 0x0001
    buf.question_type  = 0x0021
    buf.flags          = 0x0010
    buf.question_count = 0x0001
    buf.question_name  = " CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    pkt = struct.pack("!HHHHHH34sHH",buf.transaction_id,buf.flags, buf.question_count, \
                      buf.answer_count, buf.name_service_cout, buf.additional_record_count,\
                      buf.question_name,buf.question_type,buf.question_class)

    s.sendto(pkt, ip_port)

    data, src_addr = s.recvfrom(1024)

    print src_addr
    print data

    s.close()

main()
