.data
	#myMessage:	.asciiz	"Hello World\n"
	#myCharacter:	.byte	'm'
	#myInteger:	.word	23
	#Pi:		.float	3.14145
	myDouble:	.double	7.202
	zeroDouble:	.double 0.0

.text
	#li	$v0,	4		#this code works on byte and asciiz
	#li	$v0,	1		#this code works on word type (or integers)
	#li	$v0,	2		#this code works on float types
	ldc1	$f2,	myDouble	#this loads myDouble into a register in coproc1
	ldc1	$f0,	zeroDouble	#this loads zeroDouble into another register in coproc1 (these always need to be specified as a pair)
	
	li	$v0,	3	#code 3 is for doubles
	add.d	$f12, $f2, $f0 	#this adds both registers together and then stores in in $f12 (these registers are required since the value is double)
	#la	$a0,	myMessage
	#la	$a0,	myCharacter
	#lw	$a0,	myInteger
	#lwc1	$f12,	Pi
	syscall 		#syscall is always just the thing that says ok computer do it.