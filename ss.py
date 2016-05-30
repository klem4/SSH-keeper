#!/usr/bin/env python
# coding: utf-8

import os
import sys
import signal
import sqlite3
import argparse


OKGREEN = '\033[92m'
WARNING = '\033[93m'
BOLD = '\033[1m'
ENDC = '\033[0m'


def out(text, clr=None):
    if clr:
        text = '%s%s%s' % (clr, text, ENDC)
    print(text)


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

    def delete(self, pk):
        self.conn.execute(
            "DELETE FROM %s WHERE id = ? LIMIT 1" % self.tb_name, [pk])
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
        SELECT id, connection_data cd FROM %s WHERE cd LIKE ? ORDER BY cd""" % (
            self.tb_name)
        c.execute(sql, ['%%%s%%' % self.connection_data])
        return c.fetchall()


class SSChooser(object):
    def __init__(self, connection_data):
        self.part_or_name = connection_data
        self.mem = SSMemory(connection_data)
        self.candidates = self.mem.get_candidates()

    def save(self):
        self.mem.add(self.part_or_name)

    def delete(self, choose):
        self.mem.delete(choose[0])

    def connect(self, choose=None):
        connection_data = self.part_or_name if choose is None \
            else choose[1]
        os.system('ssh %s' % connection_data)

    def render_candidates(self):
        for i, c in enumerate(self.candidates):
            out("%d). %s" % (i + 1, c[1]), BOLD)


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
            out("Wrong input", WARNING)


# noinspection PyUnusedLocal
def sigint_handler(_signal, frame):
    out("\nBye!", OKGREEN)
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)


if __name__ == '__main__':
    # TODO: поддержка description вторым параметром
    # FIXME: help text for -h

    parser = argparse.ArgumentParser()
    parser.add_argument('user_input', default='', nargs='?')
    parser.add_argument('-d', action='store_true', dest='delete_mode')

    args = parser.parse_args()

    if args.delete_mode:
        out("* Delete mode!", WARNING)

    ui = args.user_input

    chooser = SSChooser(ui)
    if chooser.candidates:
        chooser.render_candidates()
        choose = validated_input(
            "Choose: ", parse_int, choices=range(1, len(chooser.candidates) + 1))

        choose = chooser.candidates[choose - 1]

        if args.delete_mode:
            chooser.delete(choose)
        else:
            chooser.connect(choose)
    else:
        if not ui:
            print("* Database is empty")
        elif raw_input("* No candidates found for %s, save and connect ? [y/N] " % ui) == 'y':
            chooser.save()
            chooser.connect()
