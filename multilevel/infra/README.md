# Infrastructure Blueprints

This directory contains blueprints that set up infrastructure in multiple forms. The application's infrastructure
consists of:

* NodeJS 10.6 running an HTTP server
* An FTP server, used to transfer files to the HTTP server

The following infrastructure options are available:

* [nodejs-aws-vm](nodejs-aws-vm): uses Cloudify's AWS types to create infrastructure on AWS.
* [nodejs-azure-appservice](nodejs-azure-appservice): uses an ARM template to instantiate an Azure Application Service backed by NodeJS.
* [nodejs-azure-vm](nodejs-azure-vm): creates a VM on Azure, along with resources such as a Network Security Group and a Public IP.
* [nodejs-azure-vm-arm](nodejs-azure-vm-arm): creates exactly the same resources as `nodejs-azure-vm` does, but through an ARM template rather than
using Cloudify's Azure Plugin's types.
* [nodejs-openstack](nodejs-openstack): creates infrastucture on OpenStack. 

All blueprints expose the following outputs:

* `username`: the FTP username to authenticate with
* `password`: the FTP password to authenticate with
* `endpoint`: the FTP endpoint to connect to (in the form of a URL, such as `ftp://10.0.0.5`)
* `base_url`: the HTTP endpoint for NodeJS
