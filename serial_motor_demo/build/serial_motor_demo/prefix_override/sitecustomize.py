import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/user/Athi-26532/ROS_Practice/serial_motor_demo/install/serial_motor_demo'
