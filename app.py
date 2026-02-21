# app.py
import requests
from datetime import datetime

def get_weather():
    """Fetch weather data from an API"""
    try:
        response = requests.get('https://api.github.com')
        print(f"✅ API Response: {response.status_code}")
        return response.json()
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("=" * 50)
    print("🐍 Python App Started")
    print(f"⏰ Time: {datetime.now()}")
    print("=" * 50)
    
    # This uses the 'requests' library (a dependency)
    data = get_weather()
    
    print("\n✅ App completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()
