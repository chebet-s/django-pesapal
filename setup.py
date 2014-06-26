import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pesapal',
    version='0.1',
    packages=[
        'django_pesapal'
    ],
    include_package_data=True,
    license='Beer-ware License',
    description='A django port for pesapal payment gateway.',
    long_description=README,
    url='http://www.example.com/',
    author='Billz',
    author_email='billz@xx.com',
    install_requires=[
        'Django>=1.5.4',
        'oauth2',
    ],
    dependency_links=[
        "https://github.com/odero/django-uuidfield/archive/master.zip#egg=django-uuidfield==0.5.0",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Beer-ware License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)