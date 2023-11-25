#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - an infinite loop
 * Return: 0 on success
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
/**
 * main - program entry point
 * Return: 0 on sucess
 */
int main()
{
	pid_t pid;
	int i, val;

	for (i = 0; i <= 4; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		/*else 
			sleep(2);*/
	}
	val = infinite_while();
	return (val);
}
