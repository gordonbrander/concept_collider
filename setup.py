import os
import sys
from setuptools import setup, find_packages

if sys.version_info < (2,7) or sys.version_info.major > 2:
    sys.exit('Only Python 2.7 is supported')

readme_path = os.path.join(os.path.dirname(__file__), "README.md")
with open(readme_path) as f:
    readme = f.read()

setup(
    name='concept_collider',
    version='0.0.1',
    author='Gordon Brander',
    description='',
    long_description=readme,
    license="MIT",
    url="https://github.com/gordonbrander/concept_collider",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=[
        "PyYAML",
        "twitter"
    ],
    extras_require={},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'concept_collider=collider:cmd_main'
        ]
    }
)
