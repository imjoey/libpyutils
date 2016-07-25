#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
from functools import partial 

from ssh import (remote_ssh_login, PasswordAuthException, 
                 remote_ssh_execcommand, SSHConnectException)


class SSHTest(unittest.TestCase):

    def setUp(self):
        self.username = 'root'

        self.password_ok = 'qwer1234'
        self.password_nook = '1234qwer'
        
        self.hostname_ok = '10.1.123.17'
        self.hostname_nook = '10.1.123.18' 
        
        self.timeout = 6


    def tearDown(self):
        pass

    def test_remote_ssh_login(self):
        self.assertTrue(
            remote_ssh_login(
                hostname=self.hostname_ok,
                username=self.username,
                timeout=self.timeout,
                password=self.password_ok
            )
        )
        self.assertFalse(
            remote_ssh_login(
                hostname=self.hostname_ok,
                password=self.password_nook,
                username=self.username,
                timeout=self.timeout
            )
        )
        with self.assertRaises(SSHConnectException):
            remote_ssh_login(
                hostname=self.hostname_nook,
                password=self.password_ok,
                username=self.username,
                timeout=self.timeout
                )


    def test_remote_ssh_execcommand(self):
        cmdout, cmderr = remote_ssh_execcommand(
            command='uname -r',
            hostname=self.hostname_ok,
            username=self.username,
            timeout=self.timeout,
            password=self.password_ok,
        )
        self.assertEqual('3.10.0-327.22.2.el7.x86_64\n', cmdout)


def main():
    unittest.main()

if __name__ == '__main__':
    sys.exit(int(main() or 0))