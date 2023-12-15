from setuptools import setup, find_packages

setup(
    name="gallery_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "django",
        "django-widget-tweaks",
        "django-extensions",
        "pillow"
    ]
)
