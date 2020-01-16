from setuptools import setup

setup(
    name='requests-llnw-auth',
    version='1.0.0',
    description='LLNW header-based auth plugin for Python Requests',
    long_description=open('README.md').read().strip(),
    long_description_content_type='text/markdown',
    author='Limelight Networks',
    author_email='opensource@llnw.com',
    url='https://github.com/llnw/requests-llnw-auth',
    license='Apache License 2.0',
    py_modules=['requests_llnw_auth'],
    python_requires='>=3.7',
    install_requires=['requests>=2.22.0']
)
