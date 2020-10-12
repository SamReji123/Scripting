#!/usr/bin/tclsh

set file [open "testdata.txt" r]
set file_data [read $file]
set number 0
close $file

set data [split $file_data "\n"]
foreach line $data {
    set a [regexp -all -inline {\S+} $line]

    if {[regexp "^-" $a]} {
        set outfile [open "report.txt" a]
        puts $outfile $a
        close $outfile
        incr $number
        } elseif {$number < 1 || $number > 1} {
                set c [lindex $a 1]
                puts $c
                set d [lreplace $a 1 1]
                puts $d
                set f [concat $d $c]
                set outfile1 [open "report.txt" a+]
                puts $outfile1 $f
                close $outfile1
                incr $number
                } else {
                    continue
                }
        }
