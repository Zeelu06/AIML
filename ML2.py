smarthome = {
  "count": 5,
  "smartdevices": [
    {
      "device_id": 1,
      "device_name": "Smart AC",
      "type": "air_conditioner",
      "brand": "LG",
      "active_status": "ON",
      "settings":  {
        "temperature": 18,
        "unit": "celsius",
        "mode": "Auto"
      }
    },
    {
      "device_id": 2,
      "device_name": "Smart Fan",
      "type": "fan",
      "brand": "Havells",
      "active_status": "OFF",
      "specs": {
        "fan_type": "ceiling",
        "color": "Black"
      }
    },
    {
      "device_id": 3,
      "device_name": "Smart Lights",
      "type": "lighting",
      "brand": "Philips",
      "active_status": "OFF",
      "specs": {
        "light_type": "LED lght",
        "color": "white"
      }
    },
    {
      "device_id": 4,
      "device_name": "Smart TV",
      "type": "television",
      "brand": "TCL",
      "active_status": "ON",
      "specs": {
        "screen_size_inch": 55,
        "os": "android"
      }
    },
    
    {
      "device_id": 5,
      "device_name": "Smart Refrigerator",
      "type": "refrigerator",
      "brand": "LG",
      "active_status": "ON",
      "settings": {
        "mode": "auto",
        "temperature": 15,
        "unit": "celsius"
      }
    }
  ]
}

print(smarthome["smartdevices"][0:5])
    