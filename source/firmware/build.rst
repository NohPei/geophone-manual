Installing the GeoMCU Firmware
=================================================


Getting the Source Code
----------------------------------------

1. Grab the latest GeoMCU firmware: https://geomcu.readthedocs.io/en/latest/
- GeoMCU 2.7 board, geophone sensor, power cable <-> board adapter cable


Building the Firmware
----------------------------------------
2. Follow Yuyan's set-up code to test MQTT (just to verify set-up is working) -- write out this section from her PDF
file:///C:/Users/julia/Downloads/Yuyan_Wireless%20sensor%20hardware%20setup%20tutorial%20(2).pdf

1. Grab the IP address of your computer (the device you are going to run the MQTT broker from)
- log-in to your router (IP address is on the router, unless you have a custom set-up)

- Install Visual Studio Code 
- In the extensions tab, install platformio

2. Open up the geoMCU firmware you previously downloaded.
Make the following changes:
1. Inside data/config > mqtt > clientid: change S-21 (highly recommended; especially important if you are flashing multiple boards, each board wants a new name)
- this 'S-21' is the name of the MQTT topic, which saves the data 
2. Inside data/config > mqtt > ip: change this IP address to be the IP of the mqtt broker (for instance, your laptop IP address)
3. Inside data/config > net > dns: change to the IP address of the router
4. Inside data/config > net > gateway: change to the IP address of the router
5. Inside data/config > net > ssid: SSID/Name of the Wi-Fi network
5. Inside data/config > net > key: Password of the Wi-Fi network

.. _flashing:

Flashing to the PCB
----------------------------------------
2. Connect to the ESP8266 geoMCU board by connect a serial-to-USB cable to the board with the following wiring:
ESP8266 GND <-> USB GND 
ESP8266 TX <-> USB RX 
ESP8266 RX <-> USB TX
Provide power to the geoMCU board as well through 12v barrel jack cable. 

(( later for the gain testing.... ))
3. Connect to the board over your serial port 
- For Windows, go to device manager and find the COM port
- Install and open the PuTTY 
(( working in the PuTTy terminal for 'abc dump' and 'gain gain' -- gain testing ))


3. Flash the board with the following command:
platformio run -t upload --upload-port /dev/ttyUSB0

4. Upload filesystem using this command:
platformio run -t uploadfs --upload-port /dev/ttyUSB0

5. Verify that everything is running correctly: (hit Enter, should see CMD> -- can also hit reset button board to see the startup processes)
minicom -b 115200 -D /dev/ttyUSB1


.. _flash_config:

Flashing Configuration in Bulk
--------------------------------------------------
