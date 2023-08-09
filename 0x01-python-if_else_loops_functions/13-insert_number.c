#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new_node == NULL) {
        return NULL; /* Memory allocation failed */
    }

    new_node->data = number;
    new_node->next = NULL;

    if (*head == NULL || (*head)->data >= number) {
        new_node->next = *head;
        *head = new_node;
    } else {
        listint_t *current = *head;
        while (current->next != NULL && current->next->data < number) {
            current = current->next;
        }
        new_node->next = current->next;
        current->next = new_node;
    }

    return new_node;
}
