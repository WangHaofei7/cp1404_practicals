"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
Answer: Every time I run, I can see an integer. The smallest number was 5, the largest number was 19.
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
Answer: I can see an integer from 3, 5, 7, 9. The smallest number was 3, the largest number was 9.
line 2 can't produce 4. Because it generates random numbers with a range step size of 2 and it begin from 3.
What did you see in line 3?
What was the smallest number you could have seen, what was the largest?
Answer: I can see a float number. The smallest number was 2.49, the largest number was 5,49.
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

import random
print(random.randint)