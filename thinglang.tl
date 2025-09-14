! define variable a with value 5
THIS a IS 5

! define variable b with value 10
THIS b IS 10

! define variable c as the result of a + b * 2
THIS c IS a + b * 2

! print the string "Result is: "
THINGSAY "Result is: " 

! print the value of variable c (25)
THINGSAY c

! define a function named calc
DOTHING calc GONNA

    ! define variable x inside function as 2 * 3
    THIS x IS 2 * 3

    ! print the value of x (6)
    THINGSAY x

! end of function definition
GONNAEND

! call the function calc
calc
