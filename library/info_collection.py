#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import platform

def run_main():
    module_args = dict(
            name=dict(type='str', required=True),
            cpu_info=dict(type='bool', required=True)
            )
            
    module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True,
    )

    name = module.params['name']
    include_cpu_info = module.params['cpu_info']
    
    if not name:
        module.fail_json(msg="Debug Message: " +

                "The 'name' parameter cannot be empty.")
    #Collect System Info

    result = {
            "message" : f"Hello, {name}!",
            "system" : platform.system(),
            "release" : platform.release(),
            "version" : platform.version()
            }
    cpu_info = {}
    if include_cpu_info:
      cpu_info = {
              "plaform" : platform.system(),
              "release" : platform.release(),
              "machine" : platform.machine(),
              "architecture" : platform.architecture(),
              "processor" : platform.processor()
              }
      if "aarch64" in cpu_info['processor']:
          cpu_info["note"] = "You have aarch64 processor"
      else:
          cpu_info["note"] = "Processor not known"


    module.exit_json(changed=True, result=result, cpu_info=cpu_info)

def main():
    run_main()

if __name__ == '__main__':
    main()
