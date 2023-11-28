#!/usr/bin/env ruby
puts ARGV[0].scan(/[from:(\w+)]|[to:(\w+)]|[flag:(\w+)]/).join
