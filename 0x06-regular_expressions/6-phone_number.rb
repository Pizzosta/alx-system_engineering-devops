#!/usr/bin/env ruby
# This script that matches a regexp with a 10 digit phone number
puts ARGV[0].scan(/\d{10,10}/).join
