	.data
prompt:		.asciiz	"Enter your age: "
message:	.asciiz	"\nYour age is "
	
	.text
	#prompt user to enter their age
	li 	$v0, 4
	la 	$a0, prompt
	syscall
	
	#get the users age
	li	$v0, 5
	syscall
	
	#store age in register
	move	$t0, $v0
	
	#print message
	li	$v0, 4
	la	$a0, message
	syscall
	
	#print age
	li	$v0, 1
	move	$a0, $t0
	syscall
	
	#signal the end of the program
	li	$v0, 10
	syscall