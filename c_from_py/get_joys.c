#include <stdlib.h>
#include <stdio.h>

typedef struct vel 
{
	double x;
	double y;
	double z;
	int pressed;
	
} joy_vel;

joy_vel *get_joystick_val(){

	joy_vel *j;
	joy_vel j0 = {1.0, 1.0, 2.0, 1};
	j = malloc(sizeof(joy_vel));
	*j = j0;
	return j;
}

void free_joy_vel(joy_vel *j){
	free(j);
}