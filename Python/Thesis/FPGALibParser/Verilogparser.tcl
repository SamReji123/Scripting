puts "Enter the gate name you'd like to parse"
gets stdin var
puts "Enter the exact gate name in the library"
gets stdin var1

set chan [open "sample.v"]
set out [open "$var.v" w]
set lineNumber 0
while {[gets $chan line] >= 0} {
    incr lineNumber
    if { [string equal "module $var1" $line]} {
	puts $out "// type:" 
	puts $out "`timescale 1ns/10ps"
	puts $out "`Celldefine"
	puts $out $line
        while {[gets $chan line] >= 0} {
            incr lineNumber
            if { [string equal "endmodule" $line] } {
		puts $out $line
		puts $out "`endcelldefine"
                close $out
                break
            } else {
                puts $out $line
            }
        }
    }
}
close $chan
