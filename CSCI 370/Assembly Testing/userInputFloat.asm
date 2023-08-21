	.data
prompt:		.asciiz	"Enter the value of pi: "
message:	.asciiz "\nThe value of pi is "
floatZero:	.float	0.0
	.text
	lwc1	$f4, floatZero
	
	#prompt the user to enter the value of pi
	li	$v0, 4
	la	$a0, prompt
	syscall
	
	#get the value of pi from user
	li	$v0, 6
	syscall
	
	#print the message
	li	$v0, 4
	la	$a0, message
	syscall
	
	#print the value
	li	$v0, 2
	add.s	$f12, $f0, $f4
	syscall
	
	#signal the end of the program
	li	$v0, 10
	syscall