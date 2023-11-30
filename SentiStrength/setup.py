import setuptools

setuptools.setup(
    name="sentistrength",
    version="0.0.9",
    author="Zhun Hung",
    author_email="yongzhunhung@gmail.com",
    description="Python 3 Wrapper for SentiStrength, reads a single or multiple input with options for binary class or scale output.",
    long_description_content_type="text/markdown",
    url="https://github.com/zhunhung/pysentistrength",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)