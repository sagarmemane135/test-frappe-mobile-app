from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in task_manager/__init__.py
from task_manager import __version__ as version

setup(
    name="task_manager",
    version=version,
    description="A mobile-friendly PWA task management app",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
