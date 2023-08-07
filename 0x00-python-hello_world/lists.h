#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

/**
 * struct listint_s - is the singly linked list 
 * @d: is the integer
 * @next: is the pointer to the next node
 *
 * Description: rep the singly linked list node structure for the Holberton project
 */
typedef struct listint_s
{
	int d;
	struct listint_s *next;
}

size_t print_listint(const listint_t *head);
listint_t *add_nodeint(listint_t **head, const int d);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /*LISTS_H*/
