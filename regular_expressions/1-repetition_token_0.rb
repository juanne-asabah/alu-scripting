#!/usr/bin/env ruby
#Check that an argument is passed and aapplies Oniguruma regex
if ARGV[0]
   print ARGV[0].scan(/hbt{2,5}n/).join
end
