import machine
from imu import MPU6050
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15)) # creating the object that allows for I2C communication in MicroPython
imu = MPU6050(i2c) # passing the i2c object to the MPU6050 class above. This class will handle all communications
imu.wake() # wakes up the MPU-6050 (it may have been in sleep mode)
gyro_data = imu.read_gyro_data()
print(gyro_data) # (0.346823, -0.198345, 0.023958)