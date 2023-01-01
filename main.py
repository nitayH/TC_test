import os
import subprocess
import configparser

def get_system_property(property: str):
    result = subprocess.run(["echo", f"%{property}%"], capture_output=True, text=True)
    result = os.system(f"echo %{property}%")
    return result.stdout

def main():
    print(f"project name: {os.environ['TEAMCITY_PROJECT_NAME']}\nversion: {os.environ['TEAMCITY_VERSION']}\nbuildconf: {os.environ['TEAMCITY_BUILDCONF_NAME']}\nID: {os.environ['BUILD_NUMBER']}")
    cwd = os.getcwd()
    print(f"cwd: {cwd}")
    print("this is master test")

    for key, value in os.environ.items():
        if "TEAMCITY" in key:
            print(f"{key} = {value}")





if __name__ == "__main__":
    main()
