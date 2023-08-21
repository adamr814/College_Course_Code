# 
######################### Mark the Game Board #########################
#
        .data
prompt: .asciiz  "\nEnter the next move: (0..z) "
board:  .ascii   "\n\n    . . . . . .      0 1 2 3 4 5"
        .ascii     "\n    . . . . . .      6 7 8 9 a b"
        .ascii     "\n    . . . . . .      c d e f g h"
        .ascii     "\n    . . . . . .      i j k l m n"
        .ascii     "\n    . . . . . .      o p q r s t"
        .asciiz    "\n    . . . . . .      u v w x y z\n"

offset: .half     6,   8,  10,  12,  14,  16
        .half    39,  41,  43,  45,  47,  49
        .half    72,  74,  76,  78,  80,  82
        .half   105, 107, 109, 111, 113, 115
        .half   138, 140, 142, 144, 146, 148
        .half   171, 173, 175, 177, 179, 181

#
########################## Main Program #######################
#
      .text
      .globl main
main:
      li    $t0, 36             # Mark 6 moves only.

      # Beginning of a loop
L1:   la    $a0, board
      li    $v0, 4             # Print the game board.
      syscall

      la    $a0, prompt
      li    $v0, 4
      syscall                  # Print the prompt.

      # Read the next move.
      li    $v0, 12            # Read a move (0..z).
      syscall                  # The syscall 12 is read char.

      move  $a0, $v0           # a0: the move in character
      jal   MarkMove           # Call the subroutine MarkMove.
      sub   $t0, $t0, 1        # Decrease the counter $t0 by 1.
      bnez  $t0, L1            # If not end of loop, go to L1.
           
      # Closing up
      li    $v0, 10            # Exit.
      syscall

# 
######################### Mark a Move #########################
#
# Input:  $a0 (the move in character)   
# Output: 
           
MarkMove:
      # Save data in the runtime stack.
      subu  $sp, $sp, 4        # Decrement the $sp to make space for $ra.
      sw    $ra, ($sp)         # Push/save the return address, $ra.
      subu  $sp, $sp, 4        # Decrement the $sp to make space for $t0.
      sw    $t0, ($sp)         # Push/save the $t0.
     
      # Convert the move to an integer.
      bgt   $a0, '9', L11
      sub   $t0, $a0, '0'
      j     L12
L11:  sub   $t0, $a0, 'a'
      add   $t0, $t0, 10

      # Find the offset.
L12:  mul   $t0, $t0, 2       # Each offset is two-byte long.
      lh    $t1, offset($t0)  # Load $t1 with the offset of the index $t0.

      # Mark the board.
      li    $t2, 'X'          # Put the piece ‘X’ in $t2.
      sb    $t2, board($t1)   # Put the piece at the location, board+offset.

      # Restore the data from the runtime stack.
      lw    $t0, ($sp)         # Pop/restore $t0.
      addu  $sp, $sp, 4        # Increment the $sp.
      lw    $ra, ($sp)         # Pop/restore the return address, $ra.
      addu  $sp, $sp, 4        # Increment the $sp.
      jr    $ra                # Return.
      
# 
######################### Error Checking #########################
#