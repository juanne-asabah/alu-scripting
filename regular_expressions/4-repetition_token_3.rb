#!/usr/bin/env ruby
#Check that an argument is passsed and applies Oniguruma regex
if ARGV[0]
    print ARGV[0].scan(/hbt*n/).join
end
