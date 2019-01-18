# Coding-Challenge Illumio

# Approach:

I have used Dictionary to store the data. It will have four main keys. 
1) inbound-tcp
2) inbound-ucp
3) outbound-tcp
4) outbound-ucp

and store tuples as value in the form of (port, ipaddress)

Ipaddress will be stored in the form of integer (I have used ipaddress package to convert into int) and it will also handle iprange properly like for example if min is 192.168.2.5 and max is 192.168.3.5. Then, converting to int can easily confirm 198.168.2.255 is within that range.

The all subsequent packages will be checked against one of the main keys and checked for each port & ipaddress in valid rules.



# a. how you tested your solution

I tested by adding more overlapping rules for port and ipaddress and  checked behavior

# b. any interesting coding, design, or algorithmic choices you’d like to point out

Used map (dictionary) to store data. In the given time frame. I have implemented iterative approach. It will take O(n) for n rules with early termination and run time is improved by constant of 1/4 for different combinations of direction/protocol


But my first thought was to implement binary search on ports. The idea was to store ports in sorted order for all four keys and for port range save in sorted form for the starting range. 



This would make the searching fast and easy for port for subsequent packages.

# c. any refinements or optimizations that you would’ve implemented if you had
more time

Yes, I would have implemented binary search described above if time was more. For this, it should be able store both individual ports and ranges in sorted order and while searching should be able to check "all" possible matches for ipaddress check. 

# d. anything else you’d like the reviewer to know

The code is clear and has comments to give intuition about I am trying to do. If you any questions please feel free to email me for questions (ellisa.khoja@gmail.com) and I will reply at the earliest.

# Interested Team :
1) Platform
2) Data

