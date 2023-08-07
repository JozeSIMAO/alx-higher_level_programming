#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head node
 * Return: 1 if True  or 0 else
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp2 = list;

	while (temp != NULL && temp2 != NULL)
	{
		temp = temp->next;
		temp2 = temp2->next->next;
		
		if (temp == temp2)
		{
			return (1);
		}
	}
	return (0);
}
