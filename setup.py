from setuptools import find_packages, setup

package_name = 'sicaklik_izleyici_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yazilimbaba4242',
    maintainer_email='yazilimbaba4242@gmail.com',
    description='Rastgele sicaklik yayinlayan bir sensor dugumu ve esik asimini loglayan bir izleyici dugumunden olusan ROS2 paketi.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor = sicaklik_izleyici_py.sensor:main',
            'izleyici = sicaklik_izleyici_py.izleyici:main',
        ],
    },
)
