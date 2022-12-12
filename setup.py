from str_response import __version__
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))

setup(
    name="str_response",
    version=__version__,
    description='str_response',
    classifiers=[
    ],
    keywords='str, response',
    url='git@github.com:marcelo-borghetti/package-python-str-response.git',
    packages=find_packages(exclude=['tests*', 'docs*']),
    include_package_data=True,
    license="MIT",
    zip_safe=True,
    install_requires=['numpy>=1.20.3', 'opencv-python>=4.5.0', 'typing>=3.7.4.3'],
    entry_points='''
        [console_scripts]
            str_response = str_response.__main__:main
            ''',
)
