# Infrastructure: OpenStack

This infrastructure blueprint creates resources on OpenStack.

## Prerequisites

### Plugins

* OpenStack
* [The demo plugin](../../../plugins/demo)

### Existing Resources

This blueprint assumes that the following resources exist:

* An external network (use the `external_network_name` input).
* A security group for agent VM's (use the `agent_security_group_name` input).
* A router (use the `router_name` input).
* A network connected to that router, and that Cloudify Manager can access (use the `network_name` input).
* A subnet in that network (use the `subnet_name` input).

### Secrets

See [Common OpenStack Secrets](../README.md#common-openstack-secrets) and [Common Secrets](../README.md#common-secrets) for secrets
that are assumed to exist. Note that most secrets are not required if inputs are provided.
