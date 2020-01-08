import setuptools
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
dev_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)

extras_require = {
  'dev': dev_requirements,
}

with open('README.md', 'r') as f:
  long_description = f.read()


setuptools.setup(
  name='lazy-rpc',
  version='0.1.0',
  description='rpc module',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/m0cchi/lazy-rpc',
  packages=setuptools.find_packages(exclude=[
    'test',
    'test.*',
  ]),
  install_requires=requirements,
  extras_require=extras_require,

  license='MIT',
  python_requires='>=3.0',
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
  ],

  author='m0cchi',
  author_email='m0cchi@protonmail.com',
  
)
