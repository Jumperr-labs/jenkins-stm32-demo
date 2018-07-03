#include "mbed.h"

DigitalOut led1(LED1);

InterruptIn button1(USER_BUTTON);
volatile bool button1_pressed = false; // Used in the main loop 1
volatile bool button1_enabled = true; // Used for debouncing
Timeout button1_timeout; // Used for debouncing

// Enables button when bouncing is over
void button1_enabled_cb(void)
{
    button1_enabled = true;
}

// ISR handling button pressed event
void button1_onpressed_cb(void)
{
    if (button1_enabled) { // Disabled while the button is bouncing
        button1_enabled = false;
        button1_pressed = true; // To be read by the main loop
        button1_timeout.attach(callback(button1_enabled_cb), 0.3); // Debounce time 300 ms
    }
}

int main()
{

    printf("mBed boot done\n");

    //button1.mode(PullUp); // Activate pull-up
    button1.fall(callback(button1_onpressed_cb)); // Attach ISR to handle button press event

    int idx = 0; // Just for printf below

    while(1) {
        if (button1_pressed) { // Set when button is pressed
            button1_pressed = false;
            printf("Button pressed %d\n", idx++);
            led1 = !led1;
        }
    }
}
