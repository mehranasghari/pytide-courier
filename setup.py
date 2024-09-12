from setuptools import setup, find_packages

setup(
    name='pytide-courier',
    version='0.0.1',
    author='Mehran Asghari',
    author_email='mhr.as1317@gmail.com',
    description='A simple cli app for sending email',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mehranasghari/pytide-courier',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts':[
            'pytide-courier = pytide_courier.pytide_courier :pytide_courier'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)