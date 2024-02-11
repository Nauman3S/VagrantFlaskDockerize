# VagrantFlaskDockerize

A simple yet powerful tool designed to streamline the deployment of Flask applications using Docker containers, all within an isolated VirtualBox environment managed by Vagrant and provisioned with Ansible.

## Getting Started

These instructions will guide you through setting up your local development environment to run and deploy a Flask application in a Docker container.

### Prerequisites

Ensure the following tools are installed on your system before you proceed:
- **VirtualBox**: [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- **Vagrant**: [Download Vagrant](https://developer.hashicorp.com/vagrant/downloads)

### Installation

1. **Start the Vagrant VM**  
   Change into the directory containing the `Vagrantfile` and execute the following command:
   ```
   vagrant up --provision
   ```
   This step will create and configure the guest machine as per the Vagrantfile and automatically provision it with Docker and the necessary dependencies using the included Ansible playbook.

2. **Access the Virtual Machine**  
   To SSH into the VM, use the following command:
   - **Windows (PowerShell):**
     ```
     ssh -i .\.vagrant\machines\default\virtualbox\private_key vagrant@127.0.0.1 -p 2222
     ```
   - **Linux/macOS:**
     ```
     ssh -i ./.vagrant/machines/default/virtualbox/private_key vagrant@127.0.0.1 -p 2222
     ```

Inside the VM, you can view the running Docker containers with:
```
sudo /snap/bin/docker ps
```

## Usage

This section provides detailed examples of how to use your application, including any additional steps to access its features.

### Accessing the Application

To access the Flask application, open [http://localhost:5000/](http://localhost:5000/) on your browser on the host machine.