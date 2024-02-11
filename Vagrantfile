Vagrant.configure("2") do |config|
  config.vm.box = "generic/rhel9"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.provision "shell", inline: <<-SHELL
    
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python3 get-pip.py
    /usr/local/bin/pip install ansible
  SHELL
  config.vm.provision "ansible_local" do |ansible|
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
    ansible.playbook = "playbook.yml"
    ansible.install = true
    ansible.verbose = "v"
    ansible.compatibility_mode = "2.0"
  end
end
