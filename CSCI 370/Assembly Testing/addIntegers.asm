.data
	int1:	.word	32
	int2:	.word	20

.text
	lw	$t0,	int1($zero)
	lw	$t1,	int2($zero)
	add	$t2, $t0, $t1	#t2 = t0 + t1
	
	li	$v0	1
	add	$a0, $zero, $t2
	syscall
	