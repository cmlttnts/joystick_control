from ctypes import *

get_joys_values = CDLL("./get_joys.so")

class JoyVel(Structure):
	_fields_ = [('x', c_double),
				('y', c_double),
				('z', c_double),
				('button', c_int)]


get_joys_values.get_joystick_val.restype = c_void_p

p1 = JoyVel.from_address(get_joys_values.get_joystick_val())
print(p1.x," ", p1.y," ", p1.z," ", p1.button)

get_joys_values.free_joy_vel(byref(p1))
del p1