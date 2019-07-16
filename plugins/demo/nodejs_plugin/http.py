import errno
import subprocess
import sys

from cloudify.decorators import operation
from cloudify.utils import exception_to_error_cause

from demo_common import run_subprocess


@operation
def start(ctx, port, content_dir, **kwargs):
    process = subprocess.Popen(
        args=['sudo', 'http-server', '-p', str(port)],
        cwd=content_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    ctx.instance.runtime_properties['pid'] = process.pid


@operation
def stop(ctx, **kwargs):
    pid = ctx.instance.runtime_properties.get('pid')
    if pid is None:
        ctx.logger.warning("No PID set; skipping")
        return

    try:
        run_subprocess(ctx, ['sudo', 'kill', '-9', str(pid)])
    except Exception as ex:
        _, _, tb = sys.exc_info()
        if isinstance(ex, OSError) and ex.errno == errno.ESRCH:
            ctx.logger.warning("No PID {0} found".format(pid))
        else:
            ctx.logger.exception("Failed terminating server")

    ctx.instance.runtime_properties.pop('pid')
