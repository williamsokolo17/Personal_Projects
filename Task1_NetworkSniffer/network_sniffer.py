from scapy.all import sniff, IP, TCP, UDP


def packet_callback(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        else:
            protocol = "OTHER"

        print("=" * 60)
        print(f"Source IP      : {src}")
        print(f"Destination IP : {dst}")
        print(f"Protocol       : {protocol}")
        print(f"Packet Length  : {len(packet)} bytes")

print("Network Sniffer Started...")
print("Press CTRL + C to stop.\n")

sniff(prn=packet_callback, store=False)
