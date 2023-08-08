#include "lists.h"

/**
 * check_cycle - checks if a linked list contain a cycle
 * @list: linked list to be check
 *
 * Return: 1 if it has cycle, 0 if it is not.
 */
int check_cycle(listint_t *list)
{
	listint_t *bad = list;
	listint_t *good = list;

	if(!list)
		return (0);
	while (good && bad && bad->next)
	{
		bad = bad->next;
		good = good->next->next;
		if (bad == good)
			return(1);
	}
	return (0);
}
