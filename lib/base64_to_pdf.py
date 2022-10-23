import base64, re

def decode(base64_string):
    pattern = re.compile('^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$')
    base64_string = base64_string.replace('\"','')
    if not pattern.match(base64_string):
        raise Exception("The string is not a valid Base64")
    else:
        with open('./static/result/document.pdf', 'wb') as the_File:
            the_File.write(base64.b64decode(base64_string))