
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 20 19:31:49 2016

@author: ponnaiyan

Login script to ssh into switches

"""

import sys #For live standard output on the screen
import pexpect #Expect-like operations


def main():
    """
    SSH into switches
    """


    switch_mgmt = {'ASW10-2': '172.29.164.193', 'DSW-1': '172.29.164.223', 'DSW-2': '172.29.164.224', 'PSW-4': '172.29.164.222'}

    switch_name=raw_input("\nEnter the switch name i.e like 'ASW1-1':")
    login_password = ['nbv123', 'sieme', '12345']

    for switch, ip_address in switch_mgmt.iteritems():
        if switch_name == switch:
            login_ip = ip_address
            exit

    cmd = "ssh " + "admin" + "@" + login_ip
    #cmd = "telnet -l " + "admin " + switch_ip
    print("spawning with cmd {}".format(cmd))
    child = pexpect.spawn(cmd)
    child.logfile_read=sys.stdout

    i = child.expect(['Are you sure you want to continue connecting (yes/no)?','assword: '])
    if i==0:
            child.sendline("yes")
            child.expect('assword: ')
            child.sendline(login_password[2])
    if i==1:
            child.sendline(login_password[2])
    child.expect('#')
    child.sendline('term width 511')
    child.sendline('conf t')
    child.sendline('line vty ; exec-timeout 0 ; end')
    child.expect('#')
    child.interact()

if __name__ == '__main__':
    main()
