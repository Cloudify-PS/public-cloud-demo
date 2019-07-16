from setuptools import setup

setup(
    name='demo-plugin',
    version='1.0.0',
    license=None,
    packages=[
        'vsftpd_plugin',
        'nodejs_plugin',
        'demo_common'
    ],
    description='Plugin for demo',
    install_requires=[
        'cloudify-common>=4.6'
    ]
)
