# coding: utf-8

import argparse
import sqlite3


class SSMemory(object):
    def __init__(self, name_or_part):
        self.name_or_part = name_or_part
        self.conn = sqlite3.connect('ss.db')
        self.ensure_table()

    def ensure_table(self):
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS ss_hosts ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "connection_data TEXT NOT NULL"
            ")"
        )

    def get_candidates(self):
        c = self.conn.cursor()


class SSChooser(object):
    def __init__(self, name_or_part):
        self.mem = SSMemory(name_or_part)

    def render_candidates(self):
        candidates = self.mem.get_candidates()
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name_or_part')
    args = parser.parse_args()
    name_or_part = args.name_or_part

    chooser = SSChooser(name_or_part)
    chooser.render_candidates()
