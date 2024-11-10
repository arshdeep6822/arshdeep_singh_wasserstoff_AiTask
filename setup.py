from setuptools import setup, find_packages

setup(
    name='chatbot',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
        'faiss-cpu',
        'sentence-transformers',
        'torch',
        'bs4',
        'langchain',
        'langchain_community',
        'openai',
        'python-dotenv',
        'six'
    ],
    author='Arshdeep Singh',
    author_email='deeparsh618@gmail.com',
    description='A chatbot powered by WordPress content',
    url='https://github.com/arshdeep6822/arshdeep_singh_wasserstoff_AiTask',
)