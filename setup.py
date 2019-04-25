from setuptools import setup

setup(
    name='RecoFlask',
    packages=['RecoFlask'],
    include_package_data=True,
    install_requires=[
        'flask','opencv-python','opencv-contrib-python','watchdog'
    ],
)