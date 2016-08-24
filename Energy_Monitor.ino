#include "EmonLib.h"             // Include Emon Library
EnergyMonitor emon1;             // Create an instance

void setup()
{  
  Serial.begin(9600);
  
  emon1.voltage(1, 122.22, 1.7);  // Voltage: input pin, calibration, phase_shift
  emon1.current(3, 86.511);        // Current: input pin, calibration.
}

void loop()
{
  emon1.calcVI(20,4000);         // Calculate all. No.of wavelengths, time-out
  emon1.serialprint();           // Print out all variables
}
