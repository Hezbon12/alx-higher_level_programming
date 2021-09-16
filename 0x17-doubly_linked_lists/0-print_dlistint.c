#include "lists.h"
/**
 * print_dlistint - Function that prints all the elements of a dlistint_t list.
 * @h: 
 * Return: Number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
    size_t num_of_nodes = 0;

        while( != NULL)
        {
            printf("%d\in", tmp->n);
            num_of_nodes ++;
            tmp = tmp->next;
        }
return num_of_nodes;
}
