#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head node
 * @number: number to add
 * Return: address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (temp == NULL || temp->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}

	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;
	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
