#!/usr/bin/env python
# encoding: utf-8

"""

ubuntu image id:  725d3b3b1c


runtime ubuntu container_id  9cb5673e126e
"""
docker run --name ksx_arbiter -p 10.163.8.90:27099:27017 -v /data/mongo_data/mongo_arbiter:/data/db -d mongo:3.0.1 --replSet "ksxingrs1"
