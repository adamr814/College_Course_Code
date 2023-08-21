	.data
newLine:	.asciiz	"\n"
	.text
main:
	addi	$s0, $zero, 10
	
	jal increaseMyRegister
	
	#print a new line
	li 	$v0, 4
	la 	$a0, newLine
	syscall
	
	jal printValue
	
	#signals the end of the program
	li	$v0, 10
	syscall
	
increaseMyRegister:
	#allocates space in the stack
	addi	$sp, $sp -8
	sw	$s0, 0($sp)
	sw	$ra, 4($sp) #you have to store the location of the nested procedure in the stack so you can get back to it and eventually restore it in main to use it again
	
	addi	$s0, $s0, 30
	
	#nested procedure
	jal printValue
	
	#restores space in the stack and gives the original value back to main
	lw	$s0, 0($sp)
	lw	$ra, 4($sp)
	addi	$sp, $sp, 8
	
	jr	$ra
	
printValue:
	li	$v0, 1
	move	$a0, $s0
	syscall
	
	jr	$ra