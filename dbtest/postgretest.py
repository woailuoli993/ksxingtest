#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 16/03/2017
import psycopg2


if __name__ == '__main__':
    conn = psycopg2.connect("dbname=postgres user=postgres password=kingsoft host=192.168.223.61 port=25432")
    cur = conn.cursor()
    # cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute("SELECT 1;")
    row = cur.fetchall()
    print(row)
    conn.commit()


    conn.close()