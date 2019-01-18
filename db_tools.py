

import sqlite3
import os
import uuid
import cv2
import datetime
import time

DB_PATH = "/Users/Alex/Desktop/doorduty/test_db.sqlite"
IMAGES_DIR = "/Users/Alex/Desktop/doorduty/test_images/"


def create_db():
    conn = sqlite3.connect(DB_PATH)
    myCursor = conn.cursor()

    myCursor.execute('CREATE TABLE guests(guest_guid TEXT PRIMARY KEY, name TEXT, face BLOB, images_dir TEXT);')
    myCursor.execute('CREATE TABLE visits(visit_guid TEXT PRIMARY KEY, guest_guid TEXT, time_seen TEXT, note TEXT);')
    conn.commit()

    return conn

def load_db():
    conn = sqlite3.connect(DB_PATH)
    myCursor = conn.cursor()

    return conn

def add_guest(conn, face, image):
    guest_guid = uuid.uuid4().hex # random guid as hex string
    images_path = IMAGES_DIR + guest_guid + "/"
    if not os.path.isdir(images_path):
        os.mkdir(images_path)
    cv2.imwrite(images_path + str(len(os.listdir(images_path)))+".jpg",image)

    myCursor = conn.cursor()
    sql = '''   INSERT INTO guests (guest_guid, face, images_dir)
                VALUES (?, ?, ?)'''
    myCursor.execute(sql, (guest_guid, face, images_path))

    conn.commit()
    return guest_guid

def log_visit(conn, guest_guid, note=None):
    visit_guid = uuid.uuid4().hex # random guid as hex string
    time = datetime.datetime.now().isoformat()

    myCursor = conn.cursor()
    sql = '''   INSERT INTO visits (visit_guid, guest_guid, time_seen, note)
                VALUES (?, ?, ?, ?)'''

    myCursor.execute(sql, (visit_guid, guest_guid, time, note))
    conn.commit()

# create_db()
# guest = add_guest(load_db(),"asfasfex",cv2.imread("/Users/Alex/Desktop/Alex_Fuji.jpg"))
# log_visit(load_db(), guest)
# time.sleep(5)
# log_visit(load_db(), guest)
