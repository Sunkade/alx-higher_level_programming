#include "lists.h"

/**
 * check_cycle - checks if a linked list contain a cycle
 * @list: linked list to be check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if(!list)
		return (0);

	while (slow && bad && bad->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return(1);
	}
	return (0);
}
