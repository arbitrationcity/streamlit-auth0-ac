import setuptools

setuptools.setup(
    name="streamlit-auth0-component-ac",
    version="0.2.2",
    author="Paul Marini",
    author_email="paul.marini@arbi.city",
    description="A fork of conradbez/streamlit-auth0, updated with patch from dhirajpatil19/streamlit-auth0. Changing the audience to be specifically set do we can use custom domain",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
        "python-jose == 3.3.0"
    ],
)
