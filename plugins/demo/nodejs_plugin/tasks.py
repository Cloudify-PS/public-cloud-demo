from cloudify.decorators import operation

from demo_common import run_subprocess


@operation
def create(ctx, npm_list, **kwargs):
    run_subprocess(ctx, args=['sudo', 'yum', '-y', 'install', 'nodejs'])

    for npm in npm_list:
        run_subprocess(ctx, args=['sudo', 'npm', 'install', npm, '-g'])
