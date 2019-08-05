# Infrastructure Blueprints

This directory contains blueprints that set up infrastructure in multiple forms. The application's infrastructure
consists of:

* NodeJS 10.6 running an HTTP server
* An FTP server, used to transfer files to the HTTP server

The following infrastructure options are available:

* [nodejs-aws-tf](nodejs-aws-tf): uses Terraform to create infrastructure on AWS.
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

## Secrets

### Common Secrets

* `default_private_key_path`: Location, on Cloudify Manager, of the private key that belongs to the keypair used to connect to new VM's.
* `default_linux_agent_user`: Default user to authenticate with when SSH'ing to VM's for installing Cloudify Agent.
* `default_public_key_data`: Public key (in SSH format) of the default keypair.

### Common AWS Secrets

* `aws_default_access_key_id`: Default access key ID to use.
* `aws_default_secret_access_key`: Default secret access key to use.
* `aws_default_ec2_region_name`: Default region name to use.
* `aws_default_vpc_id`: Default VPC ID to create resources in.
* `aws_default_linux_ami`: Default AMI for Linux instances.
* `aws_default_keypair_name`: Name of keypair to associate with new VM's.
* `aws_default_agents_security_group_id`: ID of the security group to associate to newly-created VM's.

### Common Azure Secrets

* `default_azure_subscription_id`: Default subscription ID to use.
* `default_azure_tenant_id`: Default tenant ID to use.
* `default_azure_client_id`: Default client ID to use.
* `default_azure_client_secret`: Default client secret to use.
* `default_azure_location`: Default Azure location to use.

### Common OpenStack Secrets

* `openstack_username`: Username for KeyStone authentication.
* `openstack_password`: Password for KeyStone authentication.
* `openstack_tenant_name`: Tenant name for KeyStone authentication.
* `openstack_auth_url`: KeyStone's URL.
* `openstack_region`: OpenStack Region to operate on.
* `external_network_name`: Name or ID of the external network.
* `default_agents_security_group`: Name of security group that belongs to all VM's that have Cloudify Agent installed.
* `openstack_default_keypair_name`: Name of keypair to associate with new VM's.
* `default_linux_image_id`: Default image to use for Linux VM's.
* `default_linux_flavour_id`: Default flavour to use for Linux VM's.
* `default_router_name`: Name of router to use.
* `default_management_network_name`: Name of the Cloudify management network.
* `default_subnet_name`: Name of subnet to connect the new VM to.
