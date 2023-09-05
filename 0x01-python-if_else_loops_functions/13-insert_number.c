#include "lists.h"
#include <stddef.h>
/**
 * @brief 
 * 
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *previous, *ListPointer, *newnode;

	newnode = malloc(sizeof(listint_t *));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;

	if (head == NULL)
	{
		write(2, "NULL Head", 10);
		return (NULL);
	}
	if (*head == NULL)
	{
		*head = newnode;
		return (*head);
	}

	ListPointer = *head;
	if (ListPointer->n >= number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	while (ListPointer && ListPointer->next && ListPointer->next->n < number)
		ListPointer = ListPointer->next;

	ListPointer->next = ListPointer->next;
	ListPointer->next = newnode;

	return (newnode);
}