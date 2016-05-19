"""A setup shim for 'rituals'"""
import os
import re
import sys
import subprocess
from datetime import datetime

try:
    url = subprocess.check_output('git remote get-url origin',
                                  stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError:
    url = '{{ cookiecutter.url }}'
else:
    url = url.decode('utf-8').strip()
    if url.endswith('.git'):
        url = url[:-4]
    if url.startswith('ssh://'):
        url = url[6:]
    url = re.sub(r'git@([^:/]+)[:/]', r'https://\1/', url)

try:
    now = '{:%Y%m%d-%H%M}'.format(datetime.now())
    version = subprocess.check_output("git describe --long --dirty='-{}' --all --always".format(now),
                                      stderr=subprocess.STDOUT, shell=True)
    version = version.decode('utf-8').strip().replace('/', '-')
except subprocess.CalledProcessError:
    filedate = os.path.getmtime(os.path.join(os.path.dirname(__file__), 'index.rst'))
    version = datetime.fromtimestamp(filedate).isoformat('-')[:16].replace(':', '').replace('-', '.')

project = dict(
    name=os.path.basename(os.path.dirname(os.path.abspath(__file__))),
    version=version,
    url=url,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    license='{{ cookiecutter.license }}',
)

if __name__ == "__main__":
    install = True
    for arg in sys.argv[1:]:
        if arg.startswith('--') and arg.lstrip('-') in project:
            print(project.get(arg.lstrip('-')))
            install = False

    if install:
        subprocess.call("pip install -r requirements.txt", shell=True)
