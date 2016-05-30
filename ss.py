#!/usr/bin/env python
# coding: utf-8

import os
import sys
import signal
import sqlite3
import argparse


# noinspection PyShadowingNames
class SSMemory(object):
    # FIXME: вынести в settings и запилить configure
    db_name = 'ss.db'
    tb_name = 'ss_hosts'

    def __init__(self, connection_data):
        self.connection_data = connection_data
        self.conn = sqlite3.connect(self.db_name)
        self.ensure_table()

    def add(self, connection_data, description=''):
        self.conn.execute(
            "INSERT OR IGNORE INTO %s VALUES(NULL, ?, ?)" % self.tb_name,
            [connection_data, description])
        self.conn.commit()

    def ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS %s
            (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              connection_data TEXT UNIQUE  NOT NULL,
              description TEXT DEFAULT ''
            )
            """ % self.tb_name)

    def get_candidates(self):
        c = self.conn.cursor()
        sql = """
        SELECT connection_data cd FROM %s WHERE cd LIKE ? ORDER BY cd""" % self.tb_name
        c.execute(sql, ['%%%s%%' % self.connection_data])
        return c.fetchall()


class SSChooser(object):
    def __init__(self, connection_data):
        self.part_or_name = connection_data
        self.mem = SSMemory(connection_data)
        self.candidates = self.mem.get_candidates()

    def save(self):
        self.mem.add(self.part_or_name)

    def connect(self, connection_data=None):
        connection_data = self.part_or_name if connection_data is None \
            else connection_data
        os.system('ssh %s' % connection_data)

    def render_candidates(self):
        for i, c in enumerate(self.candidates):
            print("%d). %s" % (i + 1, c[0]))


def parse_int(value, choices=None):
    try:
        value = int(value)
        if not choices or value in choices:
            return value
    except:
        pass


def validated_input(text, validate_func=None, *args, **kwargs):
    while True:
        result = validate_func(raw_input(text), *args, **kwargs)
        if result is not None:
            return result
        else:
            print("Wrong input")


# noinspection PyUnusedLocal
def sigint_handler(_signal, frame):
    print("\nBye!")
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)


if __name__ == '__main__':
    # FIXME: поддержка description вторым параметром
    # FIXME: поддержка delete и list ?
    # FIXME: quite ctrl+c
    parser = argparse.ArgumentParser()
    parser.add_argument('connection_data', default='', nargs='?')
    parser.add_argument('-d', action='store_true', dest='delete_mode')
    args = parser.parse_args()
    cd = args.connection_data

    chooser = SSChooser(cd)
    if chooser.candidates:
        chooser.render_candidates()
        choose = validated_input(
            "choose: ", parse_int, choices=range(1, len(chooser.candidates) + 1))

        choose = chooser.candidates[choose - 1]

        if args.delete_mode:
            pass
        else:
            chooser.connect(choose)
    else:
        if raw_input("No candidates found for %s, save and connect ? [y/N] " % cd) == 'y':
            chooser.save()
            chooser.connect()
