from setuptools import setup, find_packages

__version__ = __import__('bootstrap').__version__


description = "Bare Django app that includes Bootstrap's SCSS files as static files."


setup(
    name="django-bootstrap",
    version='.'.join([str(v) for v in __version__]),
    url="http://github.com/littleweaver/django-bootstrap",
    description=description,
    long_description=description,
    maintainer='Little Weaver Web Collective, LLC',
    maintainer_email='hello@littleweaverweb.com',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    platforms=['OS Independent'],
    install_requires=[
        'django>=1.7',
    ]
)
