#!/usr/bin/env ruby
#Check that an argument is passed and extract SMS details
if ARGV[0]
    #Scan for from, to and flags using capture groups
    sender = ARGV[0].scan(/\[from:(.*?)\]/).flatten[0]
    receiver = ARGV[0].scan(/\[to:(.*?)\]/).flatten[0]
    flags = ARGV[0].scan(/\[flags:(.*?)\]/).flatten[0]
    
    print "#{sender},#{receiver},#{flags}"
end

