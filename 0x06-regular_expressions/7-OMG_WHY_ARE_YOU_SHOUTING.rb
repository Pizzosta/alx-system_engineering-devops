#!/usr/bin/env ruby
# This script that matches a regexp in UPPERCASE only
puts ARGV[0].scan(/[A-Z]/).join
