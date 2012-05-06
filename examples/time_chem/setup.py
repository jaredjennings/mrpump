try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='time_chem',
    version='0.1dev',
    license='GPLv3 or later',
    author="Jared Jennings",
    author_email="jjennings@fastmail.fm",
    packages=['time_chem'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Environment :: Console',
        'Topic :: Communications',
    ],
    keywords='twitter bot module',
    zip_safe=True,
    entry_points="""
        [mrpump.chem]
        time=time_chem:TimeChem
    """,
    install_requires=['mrpump'],
)
