import sys
import time
import logging
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s')

from redis import StrictRedis
from rq import Worker, Queue, Connection

sys.path.append('/d1lod')
from d1lod import jobs

conn = StrictRedis(host='redis', port='6379')
queues = {
    'low': Queue('low', connection=conn),
    'medium': Queue('medium', connection=conn),
    'high': Queue('high', connection=conn)
}

if __name__ == '__main__':
    time.sleep(10)

    with Connection(conn):
        qs = [queues[q] for q in queues]
        w = Worker(qs)
        w.work()
