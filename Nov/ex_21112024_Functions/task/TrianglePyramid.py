"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

def Triangle_Pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ",end="")

        # Print asterisks for the current row
        for k in range(1 , i+1):
            print("* ",end="")
        print()

num_rows = 5
Triangle_Pyramid(num_rows)

