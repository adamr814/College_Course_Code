.data
	int1	.word	20
	int2	.word	8

.text
	lw	$s0,	int1	#s0 = 20
	lw	$s1,	int2	#s1 = 8
	
	sub	$t0, $s0, $s1	#t0 = s0 - s1 (t0 = 20 - 8)
	
	li	$t0,	1
	move	$a0, $t0 	#move the result from t0 into a0 which can be printed to the screen
	syscall