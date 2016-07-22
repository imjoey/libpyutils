#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import netifaces


def __local_ip_addrs(family):
    """get the ip addresses on this host

    Args:
        :param family: socket.AF_INET or socket.AF_INET6
    """

    ipaddr_list = []
    iface_list = netifaces.interfaces()
    for iface in iface_list:
        network_lines = netifaces.ifaddresses(iface).get(family, [])
        for network in network_lines:
            ipaddr_list.append(network['addr'])
    return ipaddr_list


def local_ipv4_addrs():
    """get the ipv4 addresses of all net interfaces on this host

    Returns: a list of ipv4 address str
    """
    return __local_ip_addrs(family=netifaces.AF_INET)


def local_ipv6_addrs():
    """get the ipv6 addresses of all net interfaces on this host

    Returns: a list of ipv6 address str
    """
    return __local_ip_addrs(family=netifaces.AF_INET6)


def local_hostnames():
    """get the local host names

    Returns: a list of host name str
    """
    return [socket.gethostname(), socket.getfqdn()]


def local_interface_names():
    """get all net interface names on localhost

    Returns: a list net interface name str
    """
    return netifaces.interfaces()


def is_valid_ipv4(ipv4_str):
    """Check if the input ipv4_str is an valid ipv6 address
    
    Returns: True/False
    """
    try:
        socket.inet_pton(socket.AF_INET, ipv4_str)
        return True
    except:
        return False


def is_valid_ipv6(ipv6_str):
    """Check if the input ipv6_str is an valid ipv6 address
    
    Returns: True/False
    """
    try:
        socket.inet_pton(socket.AF_INET6, ipv6_str)
        return True
    except:
        return False
