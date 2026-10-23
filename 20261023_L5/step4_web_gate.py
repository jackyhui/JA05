# Step 4 - Open the door from your phone.
#
# Same circuit as Step 3. Nothing to rewire.
#
# BEFORE YOU RUN IT: type the class Wi-Fi name and password on lines 16-17.
# The teacher writes them on the whiteboard. They are not in this file,
# because everyone on the internet can read this file on GitHub.
#
# Stop the program with Ctrl+C.

from machine import Pin, PWM, time_pulse_us
import network
import socket
import time

SSID = ""                 # <-- type the Wi-Fi name here, inside the quotes
PASSWORD = ""             # <-- type the Wi-Fi password here

PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

trig = Pin(13, Pin.OUT, value=0)
echo = Pin(14, Pin.IN)

servo = PWM(Pin(26))
servo.freq(50)

SOUND_SPEED = 0.0343
OPEN_ANGLE = 90
CLOSED_ANGLE = 0


def get_distance_cm():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    duration = time_pulse_us(echo, 1, 30000)
    if duration < 0:
        return None
    return duration * SOUND_SPEED / 2


def bar(count):
    for i, led in enumerate(leds):
        led.value(1 if i < count else 0)


def leds_for(distance):
    if distance is None:
        return 0
    return max(0, min(5, 5 - int(distance // 5)))


def set_angle(deg):
    servo.duty_u16(int(1638 + max(0, min(180, deg)) * 36.4))


def connect_wifi():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    if not station.isconnected():
        print("Connecting to", SSID, "...")
        station.connect(SSID, PASSWORD)
        for i in range(20):             # wait up to 10 seconds
            if station.isconnected():
                break
            time.sleep(0.5)
    if not station.isconnected():
        print("Wi-Fi FAILED. Check the name and the password on lines 16-17.")
        return None
    ip = station.ifconfig()[0]
    print("Connected. Open this on your phone:  http://" + ip + "/")
    return ip


def page(ip, distance, is_open):
    if distance is None:
        reading = "nothing in range"
    else:
        reading = "{:.0f} cm".format(distance)
    return """HTTP/1.1 200 OK
Content-Type: text/html

<html><head><meta name="viewport" content="width=device-width">
<meta http-equiv="refresh" content="2; url=/">
<title>Door</title></head>
<body style="font-family:sans-serif;text-align:center">
<h1>The door is {state}</h1>
<p>Sensor sees: {reading}</p>
<p><a href="/open" style="font-size:40px">OPEN</a></p>
<p><a href="/close" style="font-size:40px">CLOSE</a></p>
<p style="color:gray">{ip}</p>
</body></html>
""".format(state="OPEN" if is_open else "SHUT", reading=reading, ip=ip)


ip = connect_wifi()
is_open = False
set_angle(CLOSED_ANGLE)

if ip:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", 80))
    server.listen(1)
    print("Waiting for your phone...")
    try:
        while True:
            client, address = server.accept()      # waits here for the phone
            request = client.recv(1024).decode()

            if "GET /open" in request:
                is_open = True
            elif "GET /close" in request:
                is_open = False

            set_angle(OPEN_ANGLE if is_open else CLOSED_ANGLE)
            distance = get_distance_cm()
            bar(leds_for(distance))

            client.send(page(ip, distance, is_open))
            client.close()

            # Try it: open the door when the page asks AND when the sensor
            # sees somebody nearer than 15 cm.
    finally:
        server.close()
        set_angle(CLOSED_ANGLE)
        time.sleep(0.5)
        servo.deinit()
        bar(0)
