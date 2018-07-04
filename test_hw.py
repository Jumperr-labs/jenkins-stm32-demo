import unittest
import serial
import subprocess
import os
from time import sleep


class HwTest(unittest.TestCase):
    def setUp(self):
        sleep(2)
        self.serial = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
        self.serial.read(1024)
        self.restart()

    @staticmethod
    def restart():
        openocd_dir = os.environ['OPENOCD_PATH']
        openocd_bin = os.path.join(openocd_dir, 'bin', 'openocd')
        args = [openocd_bin, '-f', 'scripts/board/st_nucleo_f4.cfg', '-c', 'init', '-c', 'reset', '-c', 'exit']
        subprocess.check_call(args, cwd=openocd_dir)

    def testSanity(self):
        sleep(2)
        expected_data = 'mBed boot done\n'
        data = self.serial.read(len(expected_data))
        self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()

