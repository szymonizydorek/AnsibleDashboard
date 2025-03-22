#/usr/bin/python3
import socket
from ansible.module_utils.basic import AnsibleModule

def run_module():
    module = AnsibleModule(argument_spec={})
    result = {"message" : "Hello World"}
    module.exit_json(changed=False, result=result)

if __name__ == "__main__":
    run_module()

