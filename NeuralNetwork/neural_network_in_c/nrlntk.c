#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define INPUT_NODES 3
#define OUTPUT_NODES 1
#define TRAINING_ITERATIONS 150000

// sigmoid function
double sigmoid(double x)
{
    return (1.0 / ( 1.0 + exp(-x)));
}

// sigmoid derivative
double sigmoid_derivative(double x)
{
    return (x * (1.0 - x));
} 

// dot product
void dot_product(double* result , double* matrix_a , double* matrix_b , int rows , int cols)
{
    for (int i=0 ; i<rows ; i++)
    {
        result[i] = 0;
        for (int j=0; j<cols ; j++)
        {
            result[i]+=matrix_a[i*cols + j]*matrix_b[j];
        }

    }
}

// training
void train(double* inputs , double* outputs , double* weights , int iterations , int input_size , int output_size)
{
    double output[output_size];
    double error[output_size];
    double adjustments[output_size];
    double dot_result[input_size];

    for(int i = 0 ; i<iterations ; i++)
    {
        dot_product(dot_result,inputs,weights,input_size,1);

        for(int j =0 ; j<output_size ; j++)
        {
            output[j]=sigmoid(dot_result[j]);
        }

        for(int j=0; j<output_size; j++)
        {
            error[j]=outputs[j]-output[j];
            adjustments[j]=error[j]*sigmoid_derivative(output[j]);
        }

        for (int j=0 ; j<input_size ; j++)
        {
            for (int k=0 ; k<output_size; k++)
            {
                weights[j]=inputs[j]*adjustments[j];
            }
        }
    }
}

void think(double* inputs , double* weights , int input_size , int output_size)
{
    double dot_result[input_size];
    double output[output_size];

    dot_product(dot_result,inputs ,weights , input_size , 1);
    for (int j=0  ; j<output_size ; j++)
    {
        output[j]=sigmoid(dot_result[j]);
    }
    for (int i =0 ; i<output_size ; i++)
    {
        printf("Predicted Output: %f\n",output[i]);
    }
}


int main()
{
    srand(1);
    double weights[INPUT_NODES]={0};
    for (int i=0 ; i<INPUT_NODES ; i++)
    {
        weights[i]=((rand()/(double)RAND_MAX) * 2.0 - 1.0);
    }

    double inputs[7][INPUT_NODES]=
    {{0, 0, 0},
    {0, 0, 1},
    {0, 1, 0},
    {0, 1, 1},
    {1, 0, 0},
    {1, 0, 1},
    {1, 1, 0}};

    double outputs[7][OUTPUT_NODES]=
    {{0},
    {1},
    {1},
    {0},
    {1},
    {0},
    {0}};

    for(int i=0;i<7;i++)
    {
        train(inputs[i],outputs[i],weights , TRAINING_ITERATIONS, INPUT_NODES  ,OUTPUT_NODES);
    }

    double user_input[INPUT_NODES];
    printf("User Input One: ");
    scanf("%lf", &user_input[0]);
    printf("User Input Two: ");
    scanf("%lf", &user_input[1]);
    printf("User Input Three: ");
    scanf("%lf", &user_input[2]);

    printf("Considering Situation : %.1f , %.1f , %.1f \n",user_input[0],user_input[1],user_input[2]);

    think(user_input,weights , INPUT_NODES,OUTPUT_NODES);

    return 0 ;
}