#include "list.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked to the list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{       
         listint_t *slow = list;
         listint_t *fast = list;
         
         while (fast != NULL && fast->next != NULL)
	 {
		slow = slow->next;
		fast = fast->next->next;
		
		if (slow = fast)
		{

		return 1;
		}
	 }
 	
	return 0;
}	
