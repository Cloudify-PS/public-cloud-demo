import threading
import subprocess


class OutputConsumer(object):
    def __init__(self, out, logger, prefix):
        self.out = out
        self.logger = logger
        self.prefix = prefix
        self.consumer = threading.Thread(target=self.consume_output)
        self.consumer.daemon = True
        self.consumer.start()

    def consume_output(self):
        for line in self.out:
            self.logger.info("%s%s", self.prefix, line.rstrip('\n'))
        self.out.close()

    def join(self):
        self.consumer.join()


def run_subprocess(ctx, args, **kwargs):
    ctx.logger.info("Running command: %s", args)
    process = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kwargs)
    stdout_consumer = OutputConsumer(process.stdout, ctx.logger, '<out> ')
    rc = process.wait()
    ctx.logger.info("Return code: %d", rc)
    stdout_consumer.join()

    if rc != 0:
        raise subprocess.CalledProcessError(rc, args)
