# Article CMS Azure Deployment Analysis

## Overview

The Article CMS is a Python Flask web application that stores article data
in Azure SQL Database and article images in Azure Blob Storage. This analysis
compares Azure Virtual Machines and Azure App Service based on cost,
scalability, availability, and deployment workflow.

## Option 1: Azure Virtual Machine

### Cost

An Azure Virtual Machine provides detailed control over the selected machine
size, operating system, storage, and installed software. However, compute
charges generally continue while the virtual machine is running, even when
the application receives little or no traffic. Additional resources or costs
may also be required for monitoring, backup, networking, load balancing, and
higher availability.

### Scalability

A virtual machine can be scaled vertically by changing its size. Horizontal
scaling requires creating multiple virtual machines and configuring supporting
resources such as a load balancer, health probes, and an availability set or
availability zones. This provides flexibility, but it requires additional
infrastructure configuration and maintenance.

### Availability

A deployment that uses only one virtual machine creates a single point of
failure. Improving availability requires multiple instances and additional
Azure resources. The application owner is also responsible for maintaining the
virtual machine operating system, applying patches, monitoring capacity, and
recovering from operating system or server failures.

### Workflow

Deploying the Flask application to a virtual machine would require installing
and maintaining Python, the application dependencies, a production web server,
and potentially a reverse proxy. The deployment process would also require
operating-system administration, security configuration, patching, and process
management. A virtual machine provides maximum control, but it creates more
operational work for this application.

## Option 2: Azure App Service

### Cost

Azure App Service provides several pricing tiers, allowing a small training
application to use a relatively inexpensive App Service plan. The service
includes managed web hosting, HTTPS support, application configuration,
deployment tools, and logging. This reduces the number of supporting resources
that must be configured and maintained separately.

### Scalability

App Service can scale vertically by changing the App Service plan and can
scale horizontally by adding application instances on supported tiers.
Scaling is simpler than with a virtual machine because Azure manages the
underlying servers and platform infrastructure.

### Availability

Azure manages the operating system and platform maintenance for App Service.
Higher App Service tiers can provide multiple instances and additional
availability capabilities without requiring the application owner to manually
configure and maintain separate virtual machines.

### Workflow

App Service supports Python applications running on Linux and can install
dependencies from the project's requirements.txt file during deployment.
Application settings and secrets can be supplied as environment variables.
App Service also provides deployment integration, HTTPS, application logging,
and Log Stream without requiring direct management of the operating system.

## Selected Solution

I selected Azure App Service to deploy the Article CMS application. The
application is a standard Flask web application and does not require custom
operating-system configuration, privileged access, or specialized server
software. App Service provides the required Python hosting, environment
variables, deployment workflow, HTTPS, scaling options, and diagnostic logging
with substantially less administrative overhead than a virtual machine.

App Service is also a better match for the scope of this project because the
application already uses managed Azure SQL Database and Azure Blob Storage.
Using another managed service for the web application creates a simpler and
more consistent architecture. It allows development and troubleshooting to
focus on the Flask application rather than operating-system maintenance.

## Changes That Could Affect the Decision

I would reconsider the decision if the application required complete control
of the operating system, custom kernel or network configuration, unsupported
server software, privileged background services, or legacy dependencies that
could not run in Azure App Service. A virtual machine could also become more
appropriate if the application required specialized security agents or
software that had to be installed directly on the server.

For the current Article CMS requirements, none of those conditions apply.
The application only needs to host a Flask web interface, connect to Azure SQL
Database, store images in Azure Blob Storage, authenticate users through
Microsoft Entra ID, and produce application logs. Therefore, Azure App Service
remains the more appropriate deployment option.