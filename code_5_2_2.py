import tkinter as tk
from tkinter import ttk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pins = [18, 19, 20]

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def update_intensity(slider_value, led_index):
    duty_cycle = slider_value / 100.0
    pwm_led = GPIO.PWM(led_pins[led_index], 100)
    pwm_led.start(duty_cycle * 100)

root = tk.Tk()
root.title("LED Intensity Control")
root.geometry("400x200")

style = ttk.Style()
style.theme_use("default")

bg_color = "#f0f0f0"
slider_color = "#4caf50"
label_color = "#333333"
font_style = ("Arial", 12)

root.configure(background=bg_color)

sliders = []
for i in range(3):
    label = tk.Label(root, text=f"LED {i+1}", fg=label_color, font=font_style, bg=bg_color)
    label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

    slider = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value, index=i: update_intensity(value, index), style="Horizontal.TScale")
    slider.grid(row=i, column=1, padx=10, pady=10)
    sliders.append(slider)

    style.configure("Horizontal.TScale", troughcolor=bg_color, slidercolor=slider_color)

root.mainloop()
