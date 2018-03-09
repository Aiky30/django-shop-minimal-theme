from setuptools import find_packages, setup

setup(
    name='django-shop-minimal-theme',
    version='0.0.1',
    long_description='README.md',
    description='A theme for Django shop that has minimal requirements to run and should provide a good starting point for developers who wish to build their own customised shop.',
    license='LGPL',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.11,<1.12',
        'django-shop==0.11.7',
    ],
    url='',
    author='Andrew Aikman',
    author_email='aiky30@yahoo.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ]
)
