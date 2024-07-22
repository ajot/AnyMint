# AnyMint - Internet Status Checker for Mac
The WiFi indicator on the menubar can be misleading. Even though it says you're connected to WiFi, doesn't always mean you're connected to the internet. This is especially true when on train/flight/hotel WiFi.

**AnyMint** continuously monitors your internet connection by pinging Google and visually displays the status using the AnyBar application. It changes the AnyBar icon to green when the connection is successful, showing the ping time, and to red when there's a timeout.

![](https://github.com/ajot/menubar-wifi-status/blob/master/assets/demo.gif)

AnyMint is built on top of [AnyBar](https://github.com/tonsky/AnyBar) - a tiny Mac app that does one simple thing: it displays a colored dot on the menubar. What the dot means and when to change it is up to you.

## Setup AnyMint

1. Install AnyBar
```
brew install --cask anybar
```

2. Clone this repo
```
git clone https://github.com/ajot/AnyMint.git
```

## Requirements
- Python 3
- AnyBar application
- `pyanybar` Python library
- `ping3` Python library

## Installation

1. Install the required Python libraries:
   ```
   pip install pyanybar ping3
   ```

2. Install the AnyBar application. You can download it from [GitHub](https://github.com/tonsky/AnyBar) or use Homebrew:
   ```
   brew install --cask anybar
   ```

3. Save the Python script as `check-internet-status.py` in your preferred location.

## Usage

To run the script manually:

```
python check-internet-status.py
```

## Automatic Startup (macOS)

To have the script run automatically at login:

1. Open Automator and create a new Application.
2. Add a "Run Shell Script" action.
3. Set the shell to `/usr/bin/python3`.
4. Paste the script content or call the script file.
5. Save the Automator application.
6. Add the Automator application to your Login Items in System Preferences > Users & Groups.

![alt text](assets/CleanShot-2024-07-22-10-36-48@2x.png)

## Configuration

- The script is set to ping Google (`google.com`) by default. You can change this in the `check_ping` function.
- The AnyBar port is set to 1738. Modify the `port` variable if needed.
- The script checks the connection every 5 seconds. Adjust the `sleep(5)` line to change this interval.

## Troubleshooting

- Ensure AnyBar is running before starting the script.
- Check that the AnyBar port matches in both the application and the script.
- For issues with Python libraries, ensure they are correctly installed in your Python environment.

## Acknowledgments

- AnyBar project: https://github.com/tonsky/AnyBar
- pyanybar library
- ping3 library
```