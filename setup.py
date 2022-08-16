#!/usr/bin/env python3
import os
import sys

from setuptools import find_packages, setup

import deepl_translator


def get_version():
    return deepl_translator.__version__


try:
    version = get_version()
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__, 'deepl_translator')))
    version = get_version()

install_requires = [
    i for i in str(open(
        'requirements.txt', 'r', encoding='utf-8'
    ).read()).split('\n')
]

setup(name='deepl_translator',
      version=version,
      url='https://github.com/codefather-labs/deepl-translator-pyppeteer/',
      author='www.codefather.dev',
      description="Deepl translator based on pyppeteer.",
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      zip_safe=False,
      license='GNU General Public License v3.0 License',
      )