#/usr/bin/python3
import socket
import csv
import platform
from ansible.module_utils.basic import AnsibleModule

def main():

    #Ansible uses Pyhon class Ansible Module from ansible_module_utils
    module = AnsibleModule(
        argument_spec=dict(
            )
        )
   
    platform_system = platform.system()


    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    fqdn = socket.getfqdn()

    facts = {
            "hostname": hostname,
            "ip_address": ip_address,
            "FQDN": fqdn
            }

    platform_info = {
            "platform" : platform_system
            }

    log_info = {}

    if hostname == "WebServer01":
        log_info["message"] = "This is WebServer machine"
    else:
        log_info["message"] = "This is not WebServer machine"

    module.exit_json(changed=False, platform=platform_info,  result=facts, log=log_info)

if __name__ == "__main__":
    main()
