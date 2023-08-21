	.data
prompt:		.asciiz "\n\nEnter Your Move: (0..z) "
prompt2:	.asciiz "  Player X's Turn "
prompt3:	.asciiz "  Player O's Turn "
prompt4:	.asciiz	"\n*** Repeated move ***"
winMessage:	.asciiz	"\nYou Won The Game!\n"

board:		.ascii   "\n\n    . . . . . .      0 1 2 3 4 5"
	        .ascii     "\n    . . . . . .      6 7 8 9 a b"
	        .ascii     "\n    . . . . . .      c d e f g h"
	        .ascii     "\n    . . . . . .      i j k l m n"
	        .ascii     "\n    . . . . . .      o p q r s t"
	        .asciiz    "\n    . . . . . .      u v w x y z\n"
	        
offset: 	.half      6,   8,  10,  12,  14,  16
	        .half     39,  41,  43,  45,  47,  49
	        .half     72,  74,  76,  78,  80,  82
	        .half    105, 107, 109, 111, 113, 115
	        .half    138, 140, 142, 144, 146, 148
	        .half    171, 173, 175, 177, 179, 181
	        
won:    	.ascii   "1237el6ci                        "      # 0
        	.ascii   "0232348fm7dj                     "      # 1
        	.ascii   "0131343459gn8ek                  "      # 2
        	.ascii   "0121242459fl8di                  "      # 3
        	.ascii   "123235agm9ej                     "      # 4
        	.ascii   "234bhnafk                        "      # 5
        	.ascii   "7890ciciodkr                     "      # 6
        	.ascii   "68989a0elels1djdjp               "      # 7
        	.ascii   "67979a9ab2ekekq3di1fmfmt         "      # 8
        	.ascii   "67878a8ab2gn3flflrejo4ej         "      # 9
        	.ascii   "78989b4gmgmsfkp5fk               "      # a
        	.ascii   "89a5hnhntglq                     "      # b
        	.ascii   "def06i6ioioujqx                  "      # c
        	.ascii   "cefefg6krkry17j7jpjpv38i         "      # d
        	.ascii   "cdfdfgfgh07l7lslsz28k8kqkqw49j9jo"      # e
        	.ascii   "cdedegegh18m8mt39l9lrlrx5akakpkpu"      # f
        	.ascii   "defefh29n4amamsmsylqvblq         "      # g
        	.ascii   "efg5bnbntntzmrw                  "      # h
        	.ascii   "06c6cocou38djkl                  "      # i
        	.ascii   "iklklmcqx17d7dpdpv49e9eo         "      # j
        	.ascii   "ijljlmlmn6drdry28e8eqeqw5afafpfpu"      # k
        	.ascii   "ijkjkmkmn07e7esesz39f9frfrxbgqgqv"      # l
        	.ascii   "jklkln18f8ft4agagsgsyhrw         "      # m
        	.ascii   "klm29g5bhbhthtz                  "      # n
        	.ascii   "6ciciu9ejpqr                     "      # o
        	.ascii   "oqrqrs7djdjvafkfku               "      # p
        	.ascii   "oprprsrstcjx8ekekwbglglv         "      # q
        	.ascii   "opqpqrqst6dkdky9flflxhmw         "      # r
        	.ascii   "pqrqrt7elelzagmgmy               "      # s
        	.ascii   "qrs8fmbhnhnz                     "      # t
        	.ascii   "ciofkpvwx                        "      # u
        	.ascii   "uwxwxydjpglq                     "      # v
        	.ascii   "uvxvxyxyzekqhmr                  "      # w
        	.ascii   "uvwvwywyzcjqflr                  "      # x
        	.ascii   "vwxwxzdkrgms                     "      # y
        	.ascii   "wxyelshnt                        "      # z
        	
	.text
	.globl main
	
main:
	move	$t3, $zero
loop:
	beq	$t3, $zero, p2
	
p3:	li	$v0, 4			#print player o turn
	la	$a0, prompt3
	syscall
	j	br1			#can be j or b
	
p2:	li	$v0, 4			#print player x turn
	la	$a0, prompt2
	syscall
br1:					#this is the branch point where it begins to print the board/prompt
	li	$v0, 4
	la	$a0, board
	syscall
	
	li	$v0, 4
	la	$a0, prompt
	syscall
		
	li	$v0, 12
	syscall
	
	move	$s0, $v0
	move	$a0, $v0
	jal	placeMove
	
	move 	$a0, $s0		#jump to check win here
	jal	
	b 	loop
	
endProg:
	li	$v0, 10
	syscall
	
placeMove:
	subu	$sp, $sp 4
	sw	$ra, ($sp)
	subu	$sp, $sp 4
	sw 	$t0, ($sp)
	
	bgt	$a0, '9', br2
	sub	$t0, $a0, '0'
	j	br3	
br2:	sub	$t0, $a0, 'a'
	add	$t0, $t0, 10

br3:	mul	$t0, $t0, 2
	lh	$t1, offset($t0)
	
	lb	$t2, board($t1)
	beq	$t2, 46, checkMove
	li	$v0, 4
	la	$a0, prompt4
	syscall
	j	reset
	

checkMove:		
	beq 	$t3, $zero, printX
	
printO:
	li	$t2, 'O'
	sb	$t2, board($t1)
	move	$t3, $zero
	j	reset
printX:
	li	$t2, 'X'
	sb	$t2, board($t1)
	addi	$t3, $zero, 1
	j	reset

reset:	
	lw	$t0, ($sp)
	addu	$sp, $sp, 4
	lw	$ra, ($sp)
	addu	$sp, $sp, 4
	jr	$ra

CharToNum:
	blt

checkWin:
	subu	$sp, $sp, 4
	sw	$ra, ($sp)
	li	$t2, 1
	li	$t5, 3
	mul	$t1, $t0, 33