import os

def main():
    print(f"project name: {os.environ['TEAMCITY_PROJECT_NAME']}\nversion: {os.environ['TEAMCITY_VERSION']}\nbuildconf: {os.environ['TEAMCITY_BUILDCONF_NAME']}\nID: {os.environ['BUILD_NUMBER']}")


if __name__ == "__main__":
    main()
