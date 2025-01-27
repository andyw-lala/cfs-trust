# setup.py for cfsssh-setup
# Copyright 2020-2021 Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# (MIT License)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read().strip()

with open("gitInfo.txt", "r") as fh:
    long_description += '\n' + fh.read()

with open(".version", "r") as fh:
    version_str = fh.read()

package_dir = {'cfsssh':                        'src/cfsssh',
               'cfsssh.cloudinit':              'src/cfsssh/cloudinit',
               'cfsssh.setup':                  'src/cfsssh/setup',
               'cfsssh.setup.service':          'src/cfsssh/setup/service',
               'cfsssh.setup.service.liveness': 'src/cfsssh/setup/service/liveness',
               'cfsssh.setup.client':           'src/cfsssh/setup/client',}

setuptools.setup(
    name="cfs-ssh-trust",
    version=version_str,
    author="HPE Development LP",
    author_email="sps@cray.com",
    description="CFS Trust Setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cray-HPE/cfs-trust",
    package_dir = package_dir,
    packages = list(package_dir.keys()),
    keywords="vault ssh cfs kubernetes trust certificates",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
    ],
)
