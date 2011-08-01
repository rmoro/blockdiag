# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys
import pkg_resources

sys.path.insert(0, 'src')
import blockdiag

long_description = \
        open(os.path.join("src","README.txt")).read() + \
        open(os.path.join("src","TODO.txt")).read()

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

requires = ['setuptools',
            'funcparserlib',
            'webcolors']
deplinks = []

try:
    pkg_resources.get_distribution('PIL')
    requires.append('PIL')
except:
    if os.name == 'nt':
        requires.append('Pillow')
        deplinks.append('https://bitbucket.org/shimizukawa/pillow/downloads')
    else:
        requires.append('PIL')


setup(
     name='blockdiag',
     version=blockdiag.__version__,
     description='blockdiag generate block-diagram image file from spec-text file.',
     long_description=long_description,
     classifiers=classifiers,
     keywords=['diagram','generator'],
     author='Takeshi Komiya',
     author_email='i.tkomiya at gmail.com',
     url='http://blockdiag.com/',
     license='Apache License 2.0',
     py_modules=['blockdiag_sphinxhelper'],
     packages=find_packages('src'),
     package_dir={'': 'src'},
     package_data = {'': ['buildout.cfg']},
     include_package_data=True,
     install_requires=requires,
     extras_require=dict(
         test=[
             'Nose',
             'minimock',
             'pep8',
         ],
         pdf=[
             'reportlab',
         ],
     ),
     dependency_links=deplinks,
     test_suite='nose.collector',
     tests_require=['Nose','minimock','pep8'],
     entry_points="""
        [console_scripts]
        blockdiag = blockdiag.command:main

        [blockdiag_noderenderer]
        box = blockdiag.noderenderer.box
        roundedbox = blockdiag.noderenderer.roundedbox
        diamond = blockdiag.noderenderer.diamond
        minidiamond = blockdiag.noderenderer.minidiamond
        mail = blockdiag.noderenderer.mail
        note = blockdiag.noderenderer.note
        cloud = blockdiag.noderenderer.cloud
        ellipse = blockdiag.noderenderer.ellipse
        beginpoint = blockdiag.noderenderer.beginpoint
        endpoint = blockdiag.noderenderer.endpoint
        actor = blockdiag.noderenderer.actor
        flowchart.database = blockdiag.noderenderer.flowchart.database
        flowchart.input = blockdiag.noderenderer.flowchart.input
        flowchart.loopin = blockdiag.noderenderer.flowchart.loopin
        flowchart.loopout = blockdiag.noderenderer.flowchart.loopout
        flowchart.terminator = blockdiag.noderenderer.flowchart.terminator
        textbox = blockdiag.noderenderer.textbox
        dots = blockdiag.noderenderer.dots
        none = blockdiag.noderenderer.none
     """,
)

