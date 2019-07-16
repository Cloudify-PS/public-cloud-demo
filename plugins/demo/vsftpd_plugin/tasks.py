import tempfile

from cloudify.decorators import operation

from demo_common import OutputConsumer, run_subprocess

CONFIG_FILE = '/etc/vsftpd/vsftpd.conf'
SERVICE_NAME = 'vsftpd'


@operation
def create(ctx, **kwargs):
    run_subprocess(ctx, args=['sudo', 'yum', '-y', 'install', 'vsftpd'])


@operation
def configure(ctx, configuration, **kwargs):
    with tempfile.NamedTemporaryFile(delete=False) as config_file:
        config_file.write('\n'.join({"{}={}".format(key, value) for key, value in configuration.items()}))
        config_file.close()

    run_subprocess(ctx, args=['sudo', 'mv', config_file.name, CONFIG_FILE])
    run_subprocess(ctx, args=['sudo', 'chown', 'root:root', CONFIG_FILE])
    run_subprocess(ctx, args=['sudo', 'systemctl', 'enable', SERVICE_NAME])


@operation
def start(ctx, **kwargs):
    run_subprocess(ctx, args=['sudo', 'systemctl', 'start', SERVICE_NAME])


@operation
def stop(ctx, **kwargs):
    run_subprocess(ctx, args=['sudo', 'systemctl', 'stop', SERVICE_NAME])


@operation
def delete(ctx, **kwargs):
    run_subprocess(ctx, args=['sudo', 'systemctl', 'disable', SERVICE_NAME])
