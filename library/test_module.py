#!/usr/bin/python3

import socket
from ansible.module_utils.basic import AnsibleModule

def get_hostname():
    """Returns hostname of target machine"""
    try:
        return socket.gethostname()  # Get the hostname of the target machine
    except Exception as e:
        return str(e)  # Return the error if it fails

def run_module():
    module = AnsibleModule(argument_spec={
        "name" : {"type":"str", "required": True}
    })
    
    # Extract the 'name' parameter from Ansible input
    name = module.params["name"]

    # Set the message based on the 'name' parameter
    if name:
        message = f"Hello {name}"
    else:
        message = "Hello World"

    # Get the hostname of the target machine
    hostname = get_hostname()

    # Prepare the result with message and hostname
    result = {
        "message": message,
        "hostname": hostname
    }

    # Send the result back to Ansible
    module.exit_json(changed=False, result=result)

if __name__ == "__main__":
    run_module()

