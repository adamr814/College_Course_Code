.data
	message:	.asciiz	"Hello World"
.text
	main:
		jal displayMessage
	#this tells the computer that the program is done
	li 	$v0, 10
	syscall
	
	displayMessage:
		li 	$v0, 4
		la 	$a0, message
		syscall
		
		jr 	$ra