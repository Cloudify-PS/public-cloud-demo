# Using ARM Templates

This directory contains example blueprints that deploy simple ARM templates.

* [generic/blueprint.yaml](generic/blueprint.yaml) can be used to deploy any ARM template: the path to the template,
and the parameters to pass to the template, are all passed as blueprint inputs.
* [mssql/blueprint.yaml](mssql/blueprint.yaml) deploys a Microsoft SQL Server instance.
* [nodejs/blueprint.yaml](nodejs/blueprint.yaml) deploys a NodeJS App Service.
* [simple-vm/blueprint.yaml](simple-vm/blueprint.yaml) deploys a virtual machine on Azure, along with additional resources
such as a Network Security Group.
