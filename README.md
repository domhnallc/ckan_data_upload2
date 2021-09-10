# CKAN_data_upload

A python module to allow data upload to an existing package in a CKAN implementation.

# Installation


1. python setup.py install
2. pip install -r requirements.txt
3. Enter the url of the CKAN site and the API key into secrets.py
4. Try python ckanupload.py for the help text to verify installation


# Usage
`ckan_upload.py -p <package_id> -d '<description>' -u '<url>' -f <file>`

- This code allows upload of a resource (i.e. a file) to a CKAN package (a folder of resources).  There must be an existing package in the CKAN setting or this will fail.
- Description and url can be blank.
- If any string contains whitespace, it must be wrapped in quotation marks.
- File must be a full path to an existing file.
- If name is left out, the resource will be named by the description.


# Example

`python3 ckanupload3.py -p YOUR-PACKAGE-ID-GOES-HERE -d 'A sample dataset' -u /a/fake/url -f  /local/path/to/dataset.csv`

