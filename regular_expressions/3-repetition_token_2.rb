#!/usr/bin/env ruby
#Check that an argument is passed and apply the Oniguruma regex
if ARGV[0]
    print ARGV[0].scan(/hbt{1,4}n/).join
end
