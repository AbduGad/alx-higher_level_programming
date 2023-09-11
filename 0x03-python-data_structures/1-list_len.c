#include "lists.h"
/**
 * list_len - Returns the number of elements in a linked `list_t` list
 * @head: head of linked list
 * Return: number of elements in list
 */
size_t list_len(const listint_t *head)
{
	size_t v;

	v = 0;
	while (head != NULL)
	{
		head = head->next;
		v++;
	}

	return (v);
}
