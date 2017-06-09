

# AnyMint
The WiFi indicator on the menubar can be misleading. Even though it says you're connected to WiFi, doesn't always mean you're connected to the internet. This is especially true when on train/flight/hotel WiFi.

**AnyMint** indicates the Internet connectivity status in the OS X menu bar, with a green or a red light.

![](https://github.com/ajot/menubar-wifi-status/blob/master/assets/demo.gif)

### Install AnyBar
 AnyBar is a small indicator for your menubar that does one simple thing: it displays a colored dot. What the dot means and when to change it is up to you.

https://github.com/tonsky/AnyBar

```
brew cask install anybar
```

### Setup AnyMint
```
git clone git@github.com:ajot/menubar-wifi-status.git
cd menubar-wifi-status
bundle install
```

Open start_any_bar.sh, and update the path to point to the main.rb file.

## Launch
    bash start_any_bar.sh

---

**TODO**: Launch at startup - https://stackoverflow.com/questions/6442364/running-script-upon-login-mac
