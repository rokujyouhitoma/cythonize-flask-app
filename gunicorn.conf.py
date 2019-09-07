import multiprocessing

proc_name = "gunicorn"

#bind = 'unix:/tmp/{0}.sock'.format(proc_name)
bind = "127.0.0.1:8000"
#backlog = 2048

#workers = 2
workers = multiprocessing.cpu_count() * 2 + 1

worker_class = "egg:meinheld#gunicorn_worker"
worker_connections = 1000
timeout = 30
keepalive = 2

debug = False
spew = False

#daemon = True
daemon = False
pidfile = "/tmp/gunicorn.pid"
umask = 0
user = None
group = None
tmp_upload_dir = None

#errorlog = '/var/log/gunicorn/error.log'
loglevel = 'debug'
#accesslog = '/var/log/gunicorn/access.log'

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    pass

def pre_exec(server):
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    server.log.info("Server is ready. Spawning workers")

def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

    import threading, sys, traceback
    id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""),
            threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename,
                lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    worker.log.debug("\n".join(code))

def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")
