2. Break statement end the current loop, and is used to end the loop immediately. Continue statement skip the current iteration of a loop and move to the next iteration. 
3.  While loop iterates the items until it gets the true one, and ends the loop instantly. 
For loop iterates all items in the loop(list, string and etc.). Whenever it gets the true one, it
doesn't end the loop. In result, checks all iterators and ends when the iterators are finished. 
4. 
list = ["RMA", "BAR", "MCI"]
for i in range(1,2):
    for x in list:
        print(x)
