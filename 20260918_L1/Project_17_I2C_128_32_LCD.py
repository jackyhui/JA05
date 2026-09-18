import socket
import time

import network
from lcd128_32 import lcd128_32

# ---------- WiFi credentials (edit these) ----------
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# ---------- i2c config ----------
clock_pin = 22
data_pin = 21
bus = 0
i2c_addr = 0x3F

# ---------- Welcome image: 32x32 smiley (column-major, bit0 = top pixel) ----------
SMILEY = bytes(
    [
        0x00,
        0x00,
        0x00,
        0x00,
        0x80,
        0xC0,
        0x60,
        0x30,
        0x18,
        0x08,
        0x0C,
        0x04,
        0x04,
        0x04,
        0x04,
        0x04,
        0x04,
        0x04,
        0x04,
        0x04,
        0x04,
        0x0C,
        0x08,
        0x18,
        0x30,
        0x60,
        0xC0,
        0x80,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0xFC,
        0x07,
        0x01,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x1E,
        0x1E,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x1E,
        0x1E,
        0x00,
        0x00,
        0x00,
        0x00,
        0x01,
        0x07,
        0xFC,
        0x00,
        0x00,
        0x00,
        0x00,
        0x3F,
        0xE0,
        0x80,
        0x00,
        0x00,
        0x00,
        0x00,
        0x38,
        0x70,
        0xE0,
        0xC0,
        0xC0,
        0xC0,
        0xC0,
        0xC0,
        0xC0,
        0xC0,
        0xC0,
        0xE0,
        0x70,
        0x38,
        0x00,
        0x00,
        0x00,
        0x00,
        0x80,
        0xE0,
        0x3F,
        0x01,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x01,
        0x03,
        0x06,
        0x0C,
        0x18,
        0x10,
        0x30,
        0x20,
        0x20,
        0x20,
        0x20,
        0x20,
        0x60,
        0x20,
        0x20,
        0x20,
        0x20,
        0x30,
        0x10,
        0x18,
        0x0C,
        0x06,
        0x03,
        0x01,
        0x00,
        0x00,
        0x00,
        0x00,
    ]
)

# ---------- LCD setup ----------
lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)


def show_welcome():
    lcd.Clear()
    lcd.Cursor(0, 6)
    lcd.Display("WELCOME!")
    lcd.ShowImage(SMILEY, x=96, page=0, width=32, height=32)


def show_lines(lines):
    lcd.Clear()
    for row in range(min(4, len(lines))):
        lcd.Cursor(row, 0)
        lcd.Display(lines[row])


def show_message(msg):
    # wrap into 4 rows x 18 chars; only chars the font knows are kept
    msg = "".join(ch if ch in CHARS else " " for ch in msg)
    lines = [msg[i : i + 18] for i in range(0, min(len(msg), 72), 18)]
    show_lines(lines if lines else [""])


CHARS = (
    "0123456789abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "!\"#$%&'()*+,-/:;<=>?@{|}~ .^_`[\\]"
)

# ---------- Boot screen ----------
show_welcome()
time.sleep(3)

# ---------- WiFi connect ----------
lcd.Clear()
lcd.Cursor(0, 0)
lcd.Display("Connecting WiFi")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    for _ in range(40):  # wait up to ~20s
        if wlan.isconnected():
            break
        time.sleep(0.5)

if wlan.isconnected():
    ip = wlan.ifconfig()[0]
    print("WiFi connected, IP:", ip)
    show_lines(["WiFi connected", ip, "Port: 80", "Open in browser"])
    time.sleep(4)
    show_message("Ready! Send me a message from the web page.")
else:
    ip = None
    print("WiFi connection failed")
    show_lines(["WiFi FAILED", "Check SSID/password", "in the code"])

# ---------- Web server ----------
PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ESP32 LCD Message</title></head>
<body style="font-family:sans-serif;max-width:480px;margin:2em auto;padding:0 1em">
<h2>Send a message to the LCD</h2>
<form method="POST" action="/">
<input name="msg" maxlength="72" size="40" placeholder="Type your message" autofocus>
<button type="submit">Display</button>
</form>
<p>{status}</p>
</body></html>"""


def url_decode(s):
    s = s.replace("+", " ")
    out = ""
    i = 0
    while i < len(s):
        if s[i] == "%" and i + 2 < len(s) + 1 and i + 3 <= len(s):
            try:
                out += chr(int(s[i + 1 : i + 3], 16))
                i += 3
                continue
            except ValueError:
                pass
        out += s[i]
        i += 1
    return out


def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 80))
    s.listen(2)
    print("Web server: http://%s/" % ip)
    while True:
        conn, addr = s.accept()
        try:
            req = conn.recv(1024).decode("utf-8", "ignore")
            status = ""
            if req.startswith("POST"):
                body = req.split("\r\n\r\n", 1)[1] if "\r\n\r\n" in req else ""
                for pair in body.split("&"):
                    if pair.startswith("msg="):
                        msg = url_decode(pair[4:])
                        print("Message:", msg)
                        show_message(msg)
                        status = "Shown on LCD: " + msg
            html = PAGE.replace("{status}", status)
            conn.send(
                "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n"
            )
            conn.sendall(html.encode("utf-8"))
        except Exception as e:
            print("request error:", e)
        finally:
            conn.close()


if ip:
    serve()
else:
    while True:
        time.sleep(1)
