#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import os

def file_exists():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
            create=dict(type='str', choices=['yes','no'], default='no')
        )
    )

    path = module.params['path']
    create = module.params['create']

    if os.path.exists(path):
        module.exit_json(changed=False, message="File exists.")
    else:
        if create == 'yes': #checking if user passed 'yes' for file creation
            try:
                #Attempt to create file
                with open(path, 'w') as f:
                    f.write("")
                module.exit_json(changed=False, message=f"File created at {path}.")

            except Exception as e:
                module.fail_json(msg=f"Failed to create file: {e}")
        else:
            module.exit_json(changed=False, msg=f"File does not exist and creation was not requested.")

if __name__ == '__main__':
    file_exists()
