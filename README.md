AnyBar WiFi Status

# AnyBar WiFi Status
Indicates the status of the WiFi in the OS X menu bar, with a green or a red light.

## Setting up
### Install AnyBar
 AnyBar is a small indicator for your menubar that does one simple thing: it displays a colored dot. What the dot means and when to change it is up to you.

```
brew cask install anybar
```

### Install AnyBar WiFi Status

```
git clone git@github.com:ajot/menubar-wifi-status.git
cd menubar-wifi-status
bundle install
```

Open start_any_bar.sh, and update the path to point to the main.rb file.


https://github.com/tonsky/AnyBar

## Launch
    bash start_any_bar.sh

---

**TODO**: Launch at startup - https://stackoverflow.com/questions/6442364/running-script-upon-login-mac
