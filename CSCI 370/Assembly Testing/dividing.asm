.data

.text
	addi	$t0, $zero, 30
	addi	$t1, $zero, 6
	
	#div	$s0, $t0, $t1 	#constants can be used as immediates rather than taking the values from registers
	div 	$t0, $t1
	
	mflo	$s0	#quotient
	mfhi	$s1	#remainder
	
	li	$v0,	1
	move	$a0, $s0
	syscall
	
	li	$v1,	1
	move	$a0, $s1
	syscall
	
	#granted there is no space in between the numbers using the second syscall prints both the quotient and the remainder