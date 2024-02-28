# VagrantFlaskDockerize

A simple yet powerful tool designed to streamline the deployment of Flask applications using Docker containers, all within an isolated VirtualBox environment managed by Vagrant and provisioned with Ansible.

## Getting Started

These instructions will guide you through setting up your local development environment to run and deploy a Flask application in a Docker container.

### Prerequisites

Ensure the following tools are installed on your system before you proceed:
- **VirtualBox**: [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- **Vagrant**: [Download Vagrant](https://developer.hashicorp.com/vagrant/downloads)

### Installation
0. Install vbguest plugin.
  `vagrant plugin install vagrant-vbguest`

1. Generate MariaDB password
- On you host machine execute:

```bash
ansible-vault encrypt_string 'yourpassword' --name 'MARIADB_PASSWORD'
```
- It will ask for a string to encrypt.

Example output with password set as `yourpassword` and the encrypted string is `yourpassword`:

```yaml
MARIADB_PASSWORD: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          39656261646430663233356330646266336263623964383536326164646163613764613065633930
          3137393465626137393334643731663933386662646338390a643732306531376536326562616435
          30363730333137623333646235623733393361363533306634613131633364343961643662613939
          3065383333326363310a623534656635363166643333326663616235623164666239373530373639
          3361
```
- Copy it to `playbook.yml` `vars` section.
- Replace the `ansible-vault` password in `vault_password_file`
- You can also change `MARIADB_DATABASE` and `MARIADB_USER` in `app/docker-compose.yml`.

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

3. Checking the VBoxGuest Plugins:
-  `lsmod | grep vboxguest`
-  `VBoxService --version`

## Usage

This section provides detailed examples of how to use your application, including any additional steps to access its features.

### Accessing the Application

To access the Flask application, open [http://localhost:5000/](http://localhost:5000/) on your browser on the host machine.

### Getting encrypted ENVs

- Execute: 
`/snap/bin/docker ps`
Example output:

```bash 
CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                    NAMES
0b4af86da650   mariadb     "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes   3306/tcp                 app-db-1
ef62bf385509   flask-app   "gunicorn -b 0.0.0.0…"   3 minutes ago   Up 3 minutes   0.0.0.0:5000->8000/tcp   app-app-1
```

- Attach terminal and check decrypted ENVs
```bash
sudo /snap/bin/docker exec -it app-app-1 bash
```
- Once in the container execute:
```bash
echo $MARIADB_ROOT_PASSWORD
```