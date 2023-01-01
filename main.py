import os
import subprocess

def get_system_property(property: str):
    result = subprocess.run(["echo", f"%{property}%"], capture_output=True, text=True)
    return result.stdout

def main():
    print(f"project name: {os.environ['TEAMCITY_PROJECT_NAME']}\nversion: {os.environ['TEAMCITY_VERSION']}\nbuildconf: {os.environ['TEAMCITY_BUILDCONF_NAME']}\nID: {os.environ['BUILD_NUMBER']}")
    checkout_dir = get_system_property("teamcity.build.checkoutDir")
    working_dir = get_system_property("teamcity.build.workingDir")
    build_id = get_system_property("teamcity.build.id")
    branch = get_system_property("teamcity.build.branch")
    commit = get_system_property("system.build.vcs.number")
    changed_files = get_system_property("teamcity.build.changedFiles.file")
    print(f"checkout dir: {checkout_dir}\n working dir: {working_dir}\n build id: {build_id}\n branch: {branch}\ncommit:{commit}\nchanged files: {changed_files}")


    
    print()




if __name__ == "__main__":
    main()
