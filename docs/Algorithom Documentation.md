## Software Features
- **Automating Curry maker based on giving the highest priority to the customer**
  - Argument parser :- you can pass the parameters from command line.
  - Input FileReader
  - Unit tests to validate the code is right
  - Test coverage is almost **100%**
  - Fast algorithm to prepare curry with efficient data structures

## Software best practices
1. Tried to write smaller methods
2. Ran SonarLint and pylint to find code smells and solved the issues
3. Tried to parameterize most of the dependencies
4. Wrote reusable code
5. made small commits
6. code is pushed int Github.
7. Tried to make meaningful variable names

## Scripts
- main.py

## How I solve the problem ( Main algorithm)
1. From input 3 dictionary is made to make search and update faster. [ O(1) time]
   1. customer preferences : [key = customer_idx, value = customer preference for each position in the curry list]
   2. meat preferences on each position by all customers [key :position, value : customers id]
   3. veg preferences on each position by all customers [key :position, value : customers id]

2. Now take 1 customer from customer preferences dict to make him happy
   1. the customer who have the least preferences is take as next customer.
   2. if any draw happens between to customers pick the first one

3. Now for this customer take 1 preference from his/her preference list.
   1. If there is any veg preference entry in his/her preference take it
   2. Otherwise, take his/her meat preference

4. Now we have the customer preference curry_number with curry name "M" / "V".
5. Fill our main curry_list[curry_number] with this curry_number and name. So 1 entry is filled up in our curry
6. After we fill up this position, there is a chance some other customer may have the same preference for this position.
7. So they are also happy now.
8. Remove all happy customers from customer list and their ids from meat and veg preference also
9. As the [curry_number] position is already fill up and will not be changed, 
10. Remove this position from other customers' preference, meat and veg preference. Because they cannot be made hapy in this position.
11. Now iterate from steps 2 again until all customers are happy.
12. If any of the customers' preference is empty that's mean we could not make him happy.
13. If all customer are happy return the result
14. Otherwise, no solution exists

## Dry run 
let's take this example as input 

2

1 V 2 M

1 M

Here are the 3 dictionaries and other variables update on each iteration

1. customers info - {1: {1: 'V', 2: 'M'}, 2: {1: 'M'}}
2. num of customer- 2
3. meat preference- {2: {1}, 1: {2}} 
4. veg preference- {1: {1}}
5. current happy customer - 0
6. customer_to_be_picked_next - 2 - {1: 'M'} as it has the least preference
7. curry to be picked for this customer -{'curry_number': 1, 'curry_name': 'M'}
8. Our currents result ["M", None]
9. updated customers info - {1: {2: 'M'}} 
10. Now num of customer- 1
11. meat preference- {2: {1}} 
12. veg preference- {}
13. current happy customer - 1
14. customer_to_be_picked_next - 1 - {2: 'M'} 
15. curry to be picked for this customer -{'curry_number': 2, 'curry_name': 'M'} 
16. Our currents result ["M", "M"]
17. updated customers info - {} 
18. now num of customer- 0
19. meat preference- {2: {1}} 
20. veg preference- {}
21. current happy customer - 2
22. As we made all customers happy Final Curry list is :- M M

## Issue faced
- No technical issue faced. Because technically it is easy problem.
- But issue faced on structuring the problem to human-readable format 

## Next improvement target
- To be honest, I am not happy yet with the module/class/ methods I made to make it readable.
- So I will try to make it more readable and clean whenever possible. 
- Though the test coverage is **100** percent, But I did not write tests for all module/methods.
- Writing more tests should be the next improvement target
- **Concurrency** - This code currently does not support concurrency. If huge customers come it will fail. 
- **Parallelism** - current code does not support Parallelism. Though I am Not sure if it is possible for this solution.
- **Memory** - python dict gets memory from os, if customer size huge and you have not enough memory, the code will not work. 