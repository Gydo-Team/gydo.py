from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'A Package for interacting with Discord\'s API'

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="gydo.py",
    version=VERSION,
    author="loldonut (John Heinrich)",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="Apache-2.0",
    packages=find_packages(),
    install_requires=['requests', 'schedule', 'websockets', 'aiohttp', 'nest_asyncio', 'pymitter'],
    keywords=['python', 'discord', 'gydo.py', 'discord api'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Topic :: API :: Build Tools',
    'License :: OSI Approved :: Apache License 2.0',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)