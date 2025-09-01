"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        x = min(a,b)
        y = max(a,b)
        return foo(y,y%x)

def longest_run(mylist, key):
    count=0
    max=0
    for i in range (len(mylist)):
        if mylist[i]==key:
            count=count+1
            if count>max:
                max=count
        else:
            count=0
    return max



class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    def longest(low, high):
        if low>= high:
            return Result(0,0,0,True)
        if high-low ==1:
            if mylist[low]==key:
                return Result(1,1,1, True)
            else:
                return Result(0,0,0, False)
        mid=(low+high)//2
        left = longest(low,mid)
        right = longest(mid, high)
        if left.is_entire_range and right.is_entire_range:
            return Result(high-low,high-low, high-low, True )
        l_size=left.left_size if not left.is_entire_range else (left.left_size+right.left_size)
        r_size=right.right_size if not right.is_entire_range else (left.right_size+right.right_size)
        size = max(left.longest_size, right.longest_size,left.right_size+right.left_size )
        return Result(l_size, r_size, size, False)
    return longest(0, len(mylist)).longest_size
        

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

