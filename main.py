import os
import subprocess

def get_system_property(property: str):
    result = subprocess.run(["echo", f"%{property}%"], capture_output=True, text=True)
    result = os.system(f"echo %{property}%")
    return result.stdout

def main():
    print(f"project name: {os.environ['TEAMCITY_PROJECT_NAME']}\nversion: {os.environ['TEAMCITY_VERSION']}\nbuildconf: {os.environ['TEAMCITY_BUILDCONF_NAME']}\nID: {os.environ['BUILD_NUMBER']}")
    cwd = os.getcwd()
    print(f"cwd: {cwd}")
    print("this is master test")

    if "TEAMCITY_BUILD_PROPERTIES_FILE" in os.environ:
        properties_file = os.environ["TEAMCITY_BUILD_PROPERTIES_FILE"]
        print(f"found the properties file: {properties_file}")
        with open(properties_file) as f: 
            print(f.read())
    else: 
        print("didn't find property file")




if __name__ == "__main__":
    main()
