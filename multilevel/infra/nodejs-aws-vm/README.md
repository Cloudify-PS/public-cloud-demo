# Infrastructure: AWS Using Plugin Types

This infrastructure blueprint creates AWS resources using the types available in Cloudify's
official AWS plugin.

## Prerequisites

### Plugins

* AWS
* [The demo plugin](../../../plugins/demo)

### Existing Resources

This blueprint assumes that the following resources are defined externally:

* VPC (use the input `vpc_id`)
* A security group that is assigned to all VM's having Cloudify Agents installed (use the input `agents_security_group_id`)

The reason for that is that the aforementioned are, in typical cases, likely to be managed
externally to any specific application.

### Secrets

See [Common AWS Secrets](../README.md#common-aws-secrets) and [Common Secrets](../README.md#common-secrets) for secrets
that are assumed to exist. Note that most secrets are not required if inputs are provided.
