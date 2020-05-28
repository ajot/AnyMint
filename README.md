

# AnyMint
The WiFi indicator on the menubar can be misleading. Even though it says you're connected to WiFi, doesn't always mean you're connected to the internet. This is especially true when on train/flight/hotel WiFi.

**AnyMint** indicates the Internet connectivity status in the OS X menu bar, with a green or a red dot on the menu bar.

![](https://github.com/ajot/menubar-wifi-status/blob/master/assets/demo.gif)

AnyMint is built on top of [AnyBar](https://github.com/tonsky/AnyBar) - a tiny Mac app that does one simple thing: it displays a colored dot on the menubar. What the dot means and when to change it is up to you.

AnyMint simply changes the color of the dot (green or red) by checking if you're truly connected to the internet.

## Setup AnyMint

1. Install AnyBar
```
brew cask install anybar
```

2. Clone this repo
```
git clone git@github.com:ajot/AnyMint.git
```

3. Install dependencies
```
cd AnyMint
bundle install
```

4. Open `start-any-mint.sh`, and update the path to point to the main.rb file.

## Launch
    bash start-any-mint.sh

Enjoy!

---

**TODO**: Launch at startup - https://stackoverflow.com/questions/6442364/running-script-upon-login-mac
