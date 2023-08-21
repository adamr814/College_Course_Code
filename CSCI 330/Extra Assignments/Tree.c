#include<stdlib.h> 
#include<stdio.h> 

struct myTree { 
	int val; 
	struct myTree *right, *left; 
}; 

typedef struct myTree _node; 

void INSERT(_node *(*tree), _node *item) { 
  if (!(*tree)) { 
			*tree = item; 
			return; 
  } 
  if (item->val < (*tree)->val)      INSERT(&(*tree)->left, item); 
  else if (item->val > (*tree)->val) INSERT(&(*tree)->right, item); 
}

void TRAVERSE(_node *tree) { 
  //if (tree->left != NULL) TRAVERSE(tree->left); 
  printf("%d\n",tree->val); 
  if (tree->right != NULL) TRAVERSE(tree->right); 
} 

int main(void) { 
_node *current, *root; 
int i; 
  root = NULL; 
  for (i=1; i<=10; i++) { 
 			current = (_node *)malloc(sizeof(_node)); 
 			current->left = current->right = NULL; 
 			current->val = i; 
      INSERT(&root, current);
  } 
  TRAVERSE(root); 
  return 0;
}