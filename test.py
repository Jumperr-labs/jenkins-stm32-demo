#!/usr/bin/python2
import os
import unittest
from jumper.vlab import Vlab

class TestReadInterrupt(unittest.TestCase):
    def setUp(self):
        # set up the device simulation
        self.v = Vlab(working_directory=".", print_uart=True, token="20Ew9+GBD5UwnjMZHoZgECQbEqAm5S4RlmM/GMeFvVk=")
        self.v.load("BUILD/STM32_Button_Debounce.bin")
        self.v.on_pin_level_event(self.pin_listener)
        self.is_led_on = False
        self.times_pressed = 0
        # running for a while to get the BSP done
        self.v.run_for_ms(500)
        print('Virtual device is ready')

    def tearDown(self):
        self.v.stop()

    def pin_listener(self, pin_number, pin_level):
        if pin_number == 5 and pin_level == 1:
            self.is_led_on = True
            self.times_pressed = self.times_pressed + 1

    def test_debouncer(self):
        print('Button on')
        self.v.UserButton.on()
        self.v.run_for_ms(10)
        self.v.UserButton.off()
        print('Button off')
        self.v.run_for_ms(10)
        print('Button on')
        self.v.UserButton.on()
        self.v.run_for_ms(10)
        self.v.UserButton.off()
        print('Button off')
        self.v.run_for_ms(10)
        print('Button on')
        self.v.UserButton.on()
        self.v.UserButton.off()
        print('Button off')
        self.v.run_for_ms(280)
        self.assertEqual(self.is_led_on, True)
        self.assertEqual(self.times_pressed, 1)

if __name__ == '__main__':
    unittest.main()
