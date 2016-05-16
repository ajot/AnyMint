#!/usr/bin/env ruby
require 'any_bar'
require 'net/ping'

port = 1738
any_bar = AnyBar::Client.new(port)
any_bar.color = 'red'
# any_bar.color # => 'red'

@tcp = Net::Ping::TCP.new('google.com','http') # true

puts "launching the Anybar script"

while true
  if @tcp.ping?
    puts "host replied in #{@tcp.duration}"
    any_bar.color = 'green'
  else
    puts "timeout"
    any_bar.color = 'red'
  end
  sleep 5
end