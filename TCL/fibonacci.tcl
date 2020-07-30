#!/usr/bin/tclsh

proc fibonacci {number} {
	if {$number <= 1} {
		return 1;
	}
	return [expr {[fibonacci [expr $number-1]] + [fibonacci [expr $number-2]]}];
}

puts "enter a range "
set num [gets stdin]
puts "Fibonacci series upto $num is : [fibonacci $num]"
