# https://towardsdatascience.com/create-and-publish-your-own-python-package-ea45bee41cdc
import setuptools
from os.path import dirname
from os.path import join

setuptools.setup(
  name="streamlit-xui", # should match the package folder
  version="0.0.2",
  author="Aaron Gong",
  author_email="aaronjxz@gmail.com",
  license='MIT License', # should match your chosen license
  description='Extended UI components for Streamlit',
  long_description=open(join(dirname(__file__), "README.md")).read(), # loads your README.md
  long_description_content_type="text/markdown",
  url="https://github.com/ais-one/favv",
  packages=setuptools.find_packages(), # if cherry picking, packages=['folder1', 'folder2', ...]
  include_package_data=True,
  python_requires=">=3.6",
  install_requires=[
    # By definition, a Custom Component depends on Streamlit.
    # If your component has other Python dependencies, list
    # them here.
    "streamlit >= 0.63",
  ],
  keywords=["streamlit", "sidebar", "menu", "sidemenu", "hidden"], #descriptive meta-data
  classifiers=[ # https://pypi.org/classifiers
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
    # TBD add when ready 'Framework :: Streamlit'
  ]
)
