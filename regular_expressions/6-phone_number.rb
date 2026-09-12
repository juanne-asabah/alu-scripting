#!/usr/bin/env ruby
#Matches a 10 digit phone number
#Without whitespaces
if ARGV[0]
    print ARGV[0].scan(/\A[0-9]{10}\z/).join
end
