! Example ThingLang program with comments
THIS a IS 5            ! define variable a
THIS b IS 10           ! define variable b
THIS c IS a + b * 2    ! compute c as a + b * 2

THINGSAY "Result is: "  ! print a string
THINGSAY c               ! print variable c (25)

DOTHING calc GONNA       ! define function calc
    THIS x IS 2 * 3      ! define variable x in function
    THINGSAY x           ! print x (6)
GONNAEND

calc                     ! call the function calc
