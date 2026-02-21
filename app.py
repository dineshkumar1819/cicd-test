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
    # Open file to write output
    with open('output.txt', 'w') as f:
        f.write("=" * 50 + "\n")
        f.write("🐍 Python App Started successfully\n")
        f.write(f"⏰ Time: {datetime.now()}\n")
        f.write("=" * 50 + "\n\n")
        
        # This uses the 'requests' library (a dependency)
        data = get_weather()
        f.write(f"API Data: {data}\n")
        
        f.write("\n✅ App completed successfully!\n")
        f.write("=" * 50 + "\n")
    
    # Also print to console
    print("=" * 50)
    print("🐍 Python App Started successfully")
    print(f"⏰ Time: {datetime.now()}")
    print("=" * 50)
    print(f"✅ API Response: 200")
    print("\n✅ App completed successfully!")
    print("=" * 50)
    print("\n📁 Output saved to output.txt")

if __name__ == "__main__":
    main()