#!/usr/bin/env ruby
#Check that an argument is passed and applies the Oniguruma regex
if ARGV[0]
    print ARGV[0].scan(/h.n/).join
end
