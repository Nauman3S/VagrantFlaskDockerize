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
          30386133623462313339626536646134393535313935613031353665653434623764393236633533
          3962666335306265353666303531653862343533663235350a396233663032666363393961346163
          36396534663531646366616133633865663566346239313538336537386632616237303532613431
          3336363130373363300a376361323236363439323332313537333332353866663864663233333431
          3137
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