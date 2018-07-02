#!/usr/bin/python2
import unittest
from time import sleep
from jumper.vlab import Vlab


class TestClass(unittest.TestCase):
    _FAIL = False
    _PASS = True

    def setUp(self):
        ##########################
        # change these arguments #
        ##########################
        self.fw = 'BUILD/STM32_Button_Debounce.elf'  # TODO: YOUR FW HERE
        self.timeout = 10000
        self.timeout_result = self._FAIL
        self.uart_test = True
        self.uart_test_value = 'mBed boot done'
        self.uart_test_result = self._PASS
        self.gpio_test = False
        self.gpio_test_pin = None
        self.gpio_test_value = None
        self.gpio_test_result = None
        self._is_pass = False

        # set up the device simulation
        self.v = Vlab(working_directory=".", print_uart=True, token="demo-token-for-ci")
        self.v.load(self.fw)
        self.v.on_pin_level_event(self.pin_listener)
        # running for a while to get the BSP done
        self.v.start(0)
        self.uart_data = ''
        self._condition_found = False
        self.v.stop_after_ms(self.timeout)
        self.v.resume()

    def tearDown(self):
        self.v.stop()

    def pin_listener(self, pin_number, pin_level):
        if self.gpio_test and self.gpio_test_pin == pin_number and self.gpio_test_value == pin_level:
            self._is_pass = True if self.gpio_test_result == self._PASS else False
            self._condition_found = True

    def read_from_uart(self):
        self.uart_data += self.v.uart.read()
        if self.uart_test and self.uart_test_value in self.uart_data:
            self._is_pass = True if self.uart_test_result == self._PASS else False
            self._condition_found = True

    def test_debouncer(self):
        while self.v.get_state() == 'running' and not self._condition_found:
            self.read_from_uart()
            sleep(0.1)

        self.assertEqual(self._is_pass, True)


if __name__ == '__main__':
    unittest.main()
