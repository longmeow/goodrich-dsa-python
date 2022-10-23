'''C-1.17 Had we implemented the scale function (page 25) as follows, does it work
properly?

def scale(data, factor):
    for val in data:
        val *= factor
        
Explain why or why not.

It won't work properly because the identify val in fact doesn't point to any element in data, the for loop
create a copy of data which where the val actually point to, to preserve the integrity of data.
On any given iteration, data[j] and val point to different memory addresses.
'''