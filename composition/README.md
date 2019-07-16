# Using Blueprint Composition

This directory contains examples how to use the Blueprint Composition feature, available with Cloudify 4.0+,
in order to develop multi-cloud blueprints:

* [jboss-azure.yaml](jboss-azure.yaml) deploys JBoss on Azure
* [jboss-openstack.yaml](jboss-openstack.yaml) deploys JBoss on OpenStack
* [nodejs-azure.yaml](nodejs-azure.yaml) deploys NodeJS on Azure
* [nodejs-openstack.yaml](nodejs-openstack.yaml) deploys NodeJS on OpenStack

These blueprints are modularized, making use of the following reusable files:

* [include/infra-azure.yaml](include/infra-azure.yaml) creates infrastructure on Azure
* [include/infra-openstack.yaml](include/infra-openstack.yaml) creates infrastructure on OpenStack
* [include/infra-common.yaml](include/infra-common.yaml) contains definitions that are common to both cloud environments
* [include/jboss.yaml](include/jboss.yaml) contains the application definition for JBoss
* [include/nodejs.yaml](include/nodejs.yaml) contains the application definition for NodeJS
