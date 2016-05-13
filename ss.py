# coding: utf-8

import os
import argparse
import sqlite3


class SSMemory(object):
    db_name = 'ss.db'
    tb_name = 'ss_hosts'

    def __init__(self, name_or_part):
        self.name_or_part = name_or_part
        self.conn = sqlite3.connect(self.db_name)
        self.ensure_table()

    def add(self, value):
        self.conn.execute(
            "INSERT INTO %s VALUES(NULL, ?)" % self.tb_name, [value])
        self.conn.commit()

    def ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS %s
            (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              connection_data TEXT UNIQUE  NOT NULL
            )
            """ % self.tb_name)

    def get_candidates(self):
        c = self.conn.cursor()
        sql = "SELECT connection_data cd FROM %s WHERE cd LIKE ?" % self.tb_name
        c.execute(sql, ['%%%s%%' % self.name_or_part])
        return c.fetchall()



class SSChooser(object):
    def __init__(self, name_or_part):
        self.part_or_name = name_or_part
        self.mem = SSMemory(name_or_part)
        self.candidates = self.mem.get_candidates()

    def save(self):
        self.mem.add(self.part_or_name)

    def connect(self, connection_data=None):
        connection_data = self.part_or_name if connection_data is None \
            else connection_data
        os.system('ssh %s' % connection_data)

    def render_candidates(self):
        return


def validated_input(text, validate_func=None, choices=None):
    pass


if __name__ == '__main__':
    # FIXME: name_or_part - перенаименовать
    parser = argparse.ArgumentParser()
    parser.add_argument('name_or_part')
    args = parser.parse_args()
    name_or_part = args.name_or_part

    chooser = SSChooser(name_or_part)
    if chooser.candidates:
        chooser.render_candidates()
        choose = raw_input("choose: ")
    else:
        if raw_input(
            "No candidates found for %s, "
            "save and connect ? [y/N] " % name_or_part) == 'y':
            chooser.save()
            chooser.connect()
