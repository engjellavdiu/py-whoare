from setuptools import setup, find_packages

setup(
    name='py_whoare',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'aiohttp'
    ],
    author='Engjell Avdiu',
    author_email='engjellavdiu01@gmail.com',
    description='A Python library for performing WHOIS queries on multiple domains.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/engjellavdiu/py_whoare',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
