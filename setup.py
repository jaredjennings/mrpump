try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='mrpump',
    description='A twitter bot extensible by means of eggs',
    long_description=open('README.rst').read(),
    version='0.2',
    license='GPLv3 or later',
    url='http://github.com/jaredjennings/mrpump',
    author="Jared Jennings",
    author_email="jjennings@fastmail.fm",
    packages=['mrpump'],
    scripts=['scripts/emet'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Environment :: Console',
        'Topic :: Communications',
    ],
    keywords='twitter bot',
    zip_safe=True,
    entry_points="""
        [mrpump.chem]
        ping = mrpump.ping_chem:PingChem
    """,
    install_requires=['tweepy'],
)
