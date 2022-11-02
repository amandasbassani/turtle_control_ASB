from setuptools import setup

package_name = 'turtle_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amanda',
    maintainer_email='amanda.sbassani@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_node = turtle_control.my_first_node:main',
            'draw_circle = turtle_control.draw_circle:main',
            'pose_subscriber = turtle_control.pose_subscriber:main',
            'turtle_controller = turtle_control.turtle_controller:main',
            'turtle_control_ASB = turtle_control.turtle_control_ASB:main',
            'goto_goal = turtle_control.goto_goal:main'
        ],
    },
)
