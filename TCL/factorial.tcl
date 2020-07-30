#!/usr/bin/tclsh

proc factorial {number} {
	if {$number==1}	{
		return 1;
	}
	return [expr $number * [factorial [expr $number-1]]];
}

puts "enter a number"
set num [gets stdin]
puts "Factorial of $num is : [factorial $num]"

