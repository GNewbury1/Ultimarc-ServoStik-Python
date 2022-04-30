import usb.core
import usb.util
import sys


VENDOR = 0xd209
PRODUCT = 0x1700

REQUEST_TYPE = 0x21
UM_REQUEST = 0x9
SERVOSTICK_VALUE = 0x0200
SERVOSTICK_INTERFACE = 0
MESG_LENGTH = 4
UM_TIMEOUT = 2000

class UltimarcServoStik:

    def __init__(self, device):
        self.__device = device

    def clear_drivers(self):
        device = self.__device
        for cfg in device:
            for intf in cfg:
                if device.is_kernel_driver_active(intf.bInterfaceNumber):
                    try:
                        device.detach_kernel_driver(intf.bInterfaceNumber)
                    except usb.core.USBError as e:
                        sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(intf.bInterfaceNumber, str(e)))
    
    def __set_headers(self):
        payload = [4]
        payload.append(0x00)
        payload.append(0xdd)
        return payload

    def set_axis_number(self, axis):
        device = self.__device
        self.clear_drivers()
        payload = self.__set_headers()
        if axis == 4:
            payload.append(0x00)
        elif axis == 8:
            payload.append(0x01)
        device.ctrl_transfer(REQUEST_TYPE, UM_REQUEST, SERVOSTICK_VALUE, SERVOSTICK_INTERFACE, payload, UM_TIMEOUT)
        self.clear_drivers()


if __name__ == '__main__':
    args = sys.argv
    axis = int(args[1])
    if axis != 4 and axis != 8:
        raise Exception('Axis number must be 4 or 8')
    usb_devices = usb.core.find(find_all=True, idVendor=VENDOR, idProduct=PRODUCT)
    for dev in usb_devices:
        print(f'Bus: {dev.bus}, Port: {dev.port_number}')
        servo_stik = UltimarcServoStik(dev)
        servo_stik.clear_drivers()
        servo_stik.set_axis_number(axis)
        servo_stik.clear_drivers()
    print('Set all connected servo stik devices to use {} axis'.format(axis))