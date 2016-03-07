set terminal gif animate delay 5
set output "trayecto.gif"
set xrange[-2:10]
set yrange[-2:8]
#do for [i=1:100000]{ plot 'graficar.dat' every ::1::i using 2:3}
do for [i=1:100000:50]{ plot 'graficar.dat' every ::1::i using 2:3}
quit
