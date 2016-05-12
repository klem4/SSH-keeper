# coding: utf-8

import argparse
import sqlite3


class SSMemory(object):
    db_name = 'ss.db'
    tb_name = 'ss_hosts'

    def __init__(self, name_or_part):
        self.name_or_part = name_or_part
        self.conn = sqlite3.connect(self.db_name)
        self.ensure_table()

    def ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS %s
            (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              connection_data TEXT NOT NULL
            )
            """ % self.tb_name)

    def get_candidates(self):
        c = self.conn.cursor()
        c.execute(
            "SELECT connection_data cd FROM %s WHERE cd LIKE ?" %
            self.tb_name, ("'%%%s%%'" % self.name_or_part,))


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
