#!/usr/bin/env ruby
#Check if the argument was passed and apply thr Oniguruma regex.
if ARGV[0]
     print ARGV[0].scan(/School/).join
end
