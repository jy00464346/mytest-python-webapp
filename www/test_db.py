#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Muzy'

import logging
import time

logging.basicConfig(level=logging.DEBUG)
# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# 设置日志打印格式
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
logging.getLogger('').addHandler(console)

from models import User, Blog, Comment

from transwarp import db


@db.with_transaction
def test():
    u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')

    u.insert()

    print 'new user id:', u.id

    u1 = User.find_first('where email=?', 'test@example.com')
    print 'find user\'s name:', u1.name

    u1.delete()

    u2 = User.find_first('where email=?', 'test@example.com')
    print 'find user:', u2


if __name__ == '__main__':
    db.create_engine(user='mysql', password='mysql', database='awesome')
    test()
    print time.time() , time.strptime()