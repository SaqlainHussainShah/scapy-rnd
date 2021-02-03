#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:59:07 2021

@author: saqlain
"""
"""
This file is intended to convert large pcap files to smaller using python libraries 
and storing them seperately
Libraries considered for Experimentation :
    Libpcap
    Scapy
    pyshark
"""

### Import libraries
import scapy
from scapy.all import *

### Variables
file_path = "/home/ebryx/Downloads/GW_Data/gateway_traffic/gw2/2021-01-14/tcpdump-gat15-14-Jan-2021-12-18-05.pcap"

file = rdpcap(file_path)


sessions = file.sessions()


