from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Nathan Yinka',
    author_email='oludarenathaniel@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)




# from setuptools import find_packages, setup

# setup(
#     name='mcqgenerator',  # Corrected typo in the package name
#     version='0.0.1',
#     author='Nathan Yinka',
#     author_email='oludarenathaniel@gmail.com',
#     description='A package for generating multiple choice questions using AI',
#     long_description=open('README.md').read(),  # Ensure you have a README.md file
#     long_description_content_type='text/markdown',
#     url='https://github.com/yourusername/mcqgenerator',  # Replace with your actual GitHub repo URL
#     install_requires=[
#         "openai",
#         "langchain",
#         "streamlit",
#         "python-dotenv",
#         "PyPDF2"
#     ],
#     packages=find_packages(),
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
#     python_requires='>=3.6',
# )
