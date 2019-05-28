# !python3.7
import os
from subprocess import getstatusoutput

from setuptools_setup_versions import version, install_requires

package = __file__.split('/')[-2]

# Update `setup.py` to require currently installed versions of all packages
install_requires.update_versions()

# Build
status, output = getstatusoutput(
    'py -3.7 setup.py sdist bdist_wheel upload clean --all'
    if os.name == 'nt' else
    'python3.7 setup.py sdist bdist_wheel upload clean --all'
)

error = None

if status:
    error = OSError(output)
else:
    print(output)

exec(open('./clean.py').read())

if error:
    raise error
