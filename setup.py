import io
import re
from setuptools import setup


with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('tinyfn/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='tinyfn',
    version=version,
    url='https://github.com/kelvintaywl/tinyfn',
    author='Kelvin Tay',
    author_email='kelvintaywl@gmail.com',
    maintainer='Kelvin Tay',
    maintainer_email='kelvintaywl@gmail.com',
    description='A simple utility tool to evaluate function length',
    long_description=readme,
    packages=['tinyfn'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'pygments',
        'click',
    ],
    extras_require={
        'test': [
            'flake8'
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'tinyfn = tinyfn.cli:main',
        ],
    },
)