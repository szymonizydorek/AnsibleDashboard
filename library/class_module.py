#!/usr/bin/python3
import socket
import subprocess
from ansible.module_utils.basic import AnsibleModule

class HostnameReader:
    def __init__(self):
        self.hostname = None

    def get_hostname(self):
        self.hostname = socket.gethostname()
        if self.hostname == 'WebServer01':
          return "This is WebServer"
        else:
          return "This is not a WebServer"
  
class DockerOperation:
    def __init__(self):
        self.docker = None
    
    def get_docker_status(self):
        
        result = subprocess.run(['docker', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return f"Version is {result.stdout.decode().strip()}"

def run_module():
    module = AnsibleModule(argument_spec={})
    hostname_reader = HostnameReader()
    hostname = hostname_reader.get_hostname()

    docker_reader = DockerOperation()
    docker = docker_reader.get_docker_status()

    Security = {"message" : "Hello World",
              "hostname" : hostname,
              "Docker Status" : docker
              }
    module.exit_json(changed=False, result=Security)

if __name__ == "__main__":
    run_module()
