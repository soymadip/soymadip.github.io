device_status: str = "active"
temperature: int = 38

if device_status == "active":
    if temperature > 35:
        print("HIgh temperature!")
    else:
        print("Temperatur is normal")
else:
    print("Device is offilne.")
