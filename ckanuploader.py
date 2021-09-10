import getopt
import secrets
import sys

import ckanapi

ckan = ckanapi.RemoteCKAN(secrets.ckan_url, apikey=secrets.ckan_api_key)


def get_opts():
    # Get the arguments from the command-line except the filename
    argv = sys.argv[1:]
    try:
        # Define the getopt parameters
        opts, args = getopt.getopt(argv, 'p:n:d:u:f:', ['package_id', 'name','description', 'url', 'file'])
        # Check if the options' length is 4 (can be enhanced)
        if len(opts) != 4:
            print('usage: ckan_upload.py -p <package_id> -d <description> -u <url> -f <file>')
        else:
            # Iterate the options and get the corresponding values
            for opt, arg in opts:
                print(opt, arg)
            pid = opts[0][1]
            name = opts[1][1]
            desc = opts[2][1]
            url = opts[3][1]
            file = opts[4][1]
            # print(pid)
            upload_file(pid, name, desc, url, file)
    except getopt.GetoptError:
        # Print something useful
        print('usage: ckan_upload.py -p <package_id> -d <description> -u <url> -f <file>')
        sys.exit(2)


def upload_file(package_id, name, description, url, file_to_upload):
    ckan.action.resource_create(package_id=package_id,
                                name=name, # added
                                description=description,
                                url=url,
                                upload=open(file_to_upload))


def main():
    get_opts()


main()
