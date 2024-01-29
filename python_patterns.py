"""
Simple Right-Facing Triangle 
eg : 

9

*
* *
* * * 
* * * * 
* * * * * 
* * * * * *
* * * * * * *
* * * * * * * * 
* * * * * * * * * 
"""
#taking input from user - number of rows
n=int(input())
#first loop for the number of rows
for i in range(n):
  #second loop for the number of elements in each row
  for j in range(i+1):
    #in python, default print statement ends with a newline character '\n', so we have to specify it should end with space
    print("*",end=" ")
  #mepty print statement for newline character in order to seperate rows
  print()

#====================================================================================================================================================================================================================================================================#

""" 
Hollow
eg : 

9

*
* * 
*   * 
*     * 
*       *
*         * 
*           * 
*             * 
* * * * * * * * * 
"""
#taking input from user - number of rows
n=int(input())
#first loop for the number of rows
for i in range(n):
  #second loop for the number of elements in each row
  for j in range(i+1):
    #we are checking if the inner-loop variable 'j' is at starting, ending or the outer-loop variable 'i' is at the end
    if(j==0 or j==i or i==n-1):
      #then we are printing '*'
      print("*",end=" ")
    else:
      #else we are printing spaces
      print(" ",end=" ")
  #mepty print statement for newline character in order to seperate rows
  print()
#====================================================================================================================================================================================================================================================================#

"""
Simple Right-Facing Upside Down Triangle 
eg : 

9

* * * * * * * * * 
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
#taking input from user - number of rows
n=int(input())
#first loop for number of rows
for i in range(n,0,-1):
  #second loop for number of elements. Its going from i to 0 because the elements decrease for each row
  for j in range(i,0,-1):
    #default end in print statement '\n', therefore we have to specify it should be space
    print("*",end=" ")
  #newline character for seperating the rows  
  print()

#====================================================================================================================================================================================================================================================================#

"""
Hollow
eg :

9

* * * * * * * * * 
*             * 
*           * 
*         *
*       * 
*     * 
*   * 
* * 
*
"""
#taking input from user - number of rows
n=int(input())
#first loop for number of rows
for i in range(n,0,-1):
  #second loop for number of elements. Its going from i to 0 because the elements decrease for each row
  for j in range(i,0,-1):
    #checking the inner loop variable 'j', if it is at first or last position. also checking if the 'i' variable is at extreme index
    if(j==1 or j==i or i==n):
        print("*",end=" ")
    else:
        print(" ",end=" ")
  #newline character for seperating the rows  
  print()

#====================================================================================================================================================================================================================================================================#

"""
Simple Left-Facing Triangle
eg : 

9

                 * 
               * * 
             * * * 
           * * * *
         * * * * * 
       * * * * * *
     * * * * * * * 
   * * * * * * * *
 * * * * * * * * * 
 """
#taking input from use - number of rows
n=int(input())
#first loop for number of rows
for i in range(1,n+1):
  #second loop for number of elements in each row
  for j in range(1,n+1):
    #we check if the first we are at indexes where spaces are supposed to be
    if(j<=n-i):
      #printing spaces with end = " "
      print(" ",end=" ")
    #printing star when we are the correct index
    else:
      print("*",end=" ")
  #empty print statement for newline character to seperate rows  
  print()

#====================================================================================================================================================================================================================================================================#

"""
Hollow
eg : 

9

                 * 
               * * 
             *   * 
           *     *
         *       * 
       *         *
     *           * 
   *             *
 * * * * * * * * * 
"""
#taking input from use - number of rows
n=int(input())
#first loop for number of rows
for i in range(1,n+1):
  #second loop for number of elements in each row
  for j in range(1,n+1):
    #we check if the first we are at indexes where spaces are supposed to be
    if(j<=n-i):
      #printing spaces with end = " "
      print(" ",end=" ")
    #printing star when we are the correct index
    else:
        #checking if 'j' or 'i' variable is at extreme positions, then printing '*'
        if(j==n or j==n+1-i or i==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
  #empty print statement for newline character to seperate rows  
  print()
#====================================================================================================================================================================================================================================================================#

"""
Simple Left-Facing Upside Down Triangle
eg :

9

* * * * * * * * *
  * * * * * * * *
    * * * * * * * 
      * * * * * *
        * * * * *
          * * * *
            * * *
              * * 
                * 
"""
# Taking input from the user - number of rows
n = int(input())
# First loop for the number of rows (reversed)
for i in range(n, 0, -1):
    # Second loop for the number of elements in each row
    for j in range(1, n + 1):
        # Check if we are at indexes where spaces are supposed to be
        if j <= n - i:
            # Printing spaces with end=" "
            print(" ", end=" ")
        # Printing a star when we are at the correct index
        else:
            print("*", end=" ")
    # Empty print statement for a newline character to separate rows
    print()

#====================================================================================================================================================================================================================================================================#

"""
Hollow
eg :

9

* * * * * * * * *
  *             *
    *           * 
      *         *
        *       *
          *     *
            *   *
              * * 
                *
"""
n = int(input())
# First loop for the number of rows (reversed)
for i in range(n, 0, -1):
    # Second loop for the number of elements in each row
    for j in range(1, n + 1):
        # Check if we are at indexes where spaces are supposed to be
        if j <= n - i:
            # Printing spaces with end=" "
            print(" ", end=" ")
        # Printing a star when we are at the correct index
        else:
            #checking for extreme values of i,j. then printing '*'
            if(i==n or j==n or j==n-i+1):
                print("*", end=" ")
            else:
                print(" ",end=" ")
    # Empty print statement for a newline character to separate rows
    print()
#====================================================================================================================================================================================================================================================================#
"""

"""


n=int(input()
for i in range(1,n+1):
  for j in range(1, i+1):
      print("*",end=' ')
  print()
