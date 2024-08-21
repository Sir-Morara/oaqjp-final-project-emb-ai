from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A package for emotion detection using an external API.',
    author='Sir-Morara', 
    author_email='moraragift@gmail.com',  
    url='https://github.com/Sir-Morara/oaqjp-final-project-emb-ai', 
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.11',
    ],
)
