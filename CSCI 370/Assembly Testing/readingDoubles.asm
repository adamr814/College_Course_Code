	.data
prompt:		.asciiz "Enter the value of e: "
	.text
	#display message to user
	li	$v0, 4
	la	$a0, prompt
	syscall
	
	#get double from user
	li	$v0, 7
	syscall
	
	#display user input
	li	$v0, 3
	add.d	$f12, $f0, $f10
	syscall
	
	#signal the end of the program
	li	$v0, 10
	syscall