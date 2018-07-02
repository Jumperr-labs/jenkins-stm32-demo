import unittest
import serial
import subprocess
import os
from time import sleep


class HwTest(unittest.TestCase):
    def setUp(self):
        self.serial = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
        self.restart()

    def restart(self):
        openocd_dir = os.environ['OPENOCD_PATH']
        openocd_bin = os.path.join(openocd_dir, 'bin', 'openocd')
        args = [openocd_bin, '-f', 'scripts/board/st_nucleo_f4.cfg', '-c', 'init', '-c', 'reset', '-c', 'exit']
        subprocess.check_call(args, cwd=openocd_dir)

    def testSanity(self):
        sleep(2)
        expected_data = 'mBed boot'
        data = self.serial.read(len(expected_data))
        self.assertTrue(expected_data in data)


if __name__ == '__main__':
    unittest.main()
