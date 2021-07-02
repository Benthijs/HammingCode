All code was jointly created by Amin Tahiri, Benjamin Mason and Jan-Bas Spoelder.        
  
## Hamming Code
# Introduction
Hamming code project for Programmeren in de Wiskunde final project. Suppose we send a message to a random person. We may have made a mistake in the message we wanted to send. It is also possible that we have other data that contains an error. It would be nice if this error could be detected and corrected automatically. In this project we do exactly this using the Hamming(7,4) code.
# Getting started
Clone the project
```git clone https://github.com/Benthijs/HammingCode```
# Issues
* **We cannot correct larger bit errors for the Hamming-(11,7) code**
# Future goals
In the project could have made a number of improvements and extensions. We could have checked larger data strings first by extending our code to a larger Hamming code. Furthermore, we could also have improved the code by creating functions that also take into account the fact that more than one error can be made. Our code cannot do this and therefore returns an erroneous vector if there is more than one error in the data state. We also saw a lot of errors in the calculations during the project because we had not properly defined vectors. Due to the incorrect definition, the correct dimension of the vector was not calculated, resulting in calculation errors. So we should have made a subclass that handles these vectors with more ease.
# License
None.
