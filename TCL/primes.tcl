#!/usr/bin/tclsh

proc check_prime {num} {
	if {$num>1} {
		set flag 1;
		for {set i 2} {$i<$num} {incr i} {
			if {$num%$i!=0} {
				#incr flag;
				set flag [expr $flag+1];
			} else {
				#puts "$num is not prime";
				return false;
			}
		}
		if {$flag>1 || $num==2} {
			#puts "$num is prime ";
			return true;
		}
	} else {
		#puts "Enter a num greater than 1"
		return false;
	}
}

puts "enter a range"
set num [gets stdin]

set count 0;		# holds total number of primes
set sum 0;		# holds sum of primes

#puts "Is $num prime ? : [check_prime $num] \n"
for {set n 1} {$n<$num} {incr n} {
	set prime_check [check_prime $n]
	if ($prime_check==true) {
		set count [expr $count+1];
		set sum [expr $sum+$n]
	}
}
puts "Total number of primes from 2 to $num = $count \n"
puts "Sum of primes from 2 to $num = $sum \n"

#puts "Is $num prime ? : [check_prime $num] \n"

