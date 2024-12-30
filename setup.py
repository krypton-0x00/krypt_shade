from setuptools import setup, find_packages

setup(
    name="krypt_shade",
    version="0.1",
    packages=find_packages(),
    description="A library to manipulate colors (HEX to RGB, brightness adjustment, shade generation)",
    author="krypton-0x00",
    author_email="krypton0x00@gmail.com",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/krypton-0x00/krypt_shade",  # Change this to your actual GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
