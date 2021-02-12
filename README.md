# Yoni PHSX815 HW3

The Cookie programs work. I've modified the Random class to now also do random numbers from a Logistic distribution. random_reading will plot these. 
random_writing now takes a -method argument. if the method specified is "Logistic", you can also pass -mu and -sigma, which should be the mean and
standard deviation of your desired logistic distribution. Otherwise, the program still prints output to output.txt, and the reader still reads from
output.txt