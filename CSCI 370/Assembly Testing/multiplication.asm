#this program uses various multiplication commands
.data

.text
	addi	$s0, $zero, 4
	
	sll	$t0, $s0, 2 	#this basically is exponent multiplication the value is i in this case 2^2 or 4 so sll will be 4 * 4 = 16
	
	li	$v0	1
	move	$a0, $t0
	syscall
	
	#this section uses mult and moves the result from the lo register  {
	#addi	$t0, $zero, 2000
	#addi 	$t1, $zero, 10
	
	#mult	$t0, $t1	#due to the size of the result it will stored in the lo and hi registers
	
	#mflo	$s0
	
	#li	$v0, 1
	#add	$a0, $zero, $s0
	#syscall  }		
	
	#this section uses mul  {
	#addi	$s0, $zero, 10
	#addi	$s1, $zero, 4
	
	#mul	$t0, $s0, $s1	#t0 = 10 * 4
	
	#li	$v0,	1
	#move	$a0, $t0
	#(add $a0, $zero, $t0) is also an acceptable method of moving the result to the correct register
	#syscall  }
	