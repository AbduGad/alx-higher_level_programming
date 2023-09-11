#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if the list is a palindrome
 *
 * @head: list's head
 * Return: 1 if true 0 if false
 */
int is_palindrome(listint_t **head)
{
	int listlength, flag_odd, array[(list_len(*head) / 2)], i = 0, flag = 0;
	

	flag_odd = 0;
	listlength = list_len(*head);
	listint_t *temp = *head;

	if (listlength == 0 || listlength == 1)
		return (1);

	if (listlength % 2 != 0)
		flag_odd = 1;

	while (temp)
	{
		if (i != listlength / 2 && flag == 0)
		{
			array[i] = temp->n;
			i++;
			temp = temp->next;
		}
		else
		{
			flag = 1;
			if (flag_odd)
			{
				temp = temp->next;
				flag_odd = 0;
			}
			if (temp->n != array[--i])
				return (0);
			temp = temp->next;
		}
	}
	return (1);
}

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
