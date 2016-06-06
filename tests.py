# coding: utf-8

import os
import sqlite3 from unittest import TestCase
from ssh_keeper import SKChooser, SKMemory


class CommonTestCase(TestCase):
    db_name = SKMemory.db_name
    table_name = SKMemory.db_name

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.path.unlink(self.db)
        except:
            pass

    def testNoCandidates(self):
        pass

    def testAddHost(self):
        pass

    def testRemoveHost(self):
        pass
