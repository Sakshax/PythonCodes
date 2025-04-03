'''
This code prints a pyramid pattern of stars.

    * 
   * * 
  * * * 
 * * * * 
* * * * * 

'''

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
