# One string is an anagram of another if the second is simply a rearrangement of the first.
# For example, 'heart' and 'earth' are anagrams.
# The strings 'python' and 'typhon' are anagrams as well.

# ============================================================================ #
# Solution 1: Checking Off
# ============================================================================ #

# Check to see that each character in the first string actually occurs in the second.
# If it is possible to “checkoff” each character, then the two strings must be anagrams.
# Checking off a character will be accomplished by replacing it with the special Python value None.

def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('abcd','dcba'))
# Note that each of the n characters in s1 will cause an iteration through up to
# n characters in the list from s2. Each of the n positions in the list will be
# visited once to match a character from s1.
# The number of visits then becomes the sum of the integers from 1 to n.

# Number of Iterations:
# => n(n+1)/2
# => ((n2) + n)/2

# As n gets large, the n2 term will dominate the n term and the 1/2 can be ignored.
# Therefore, this solution is O(n2).





# ============================================================================ #
# Solution 2: Sort and Compare
# ============================================================================ #

# Even though s1 and s2 are different, they are anagrams only if they consist of
# exactly the same characters.
# Begin by sorting each string alphabetically, from a to z, we will end up with
# the same string if the original two strings are anagrams

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))

# Sorting is typically either O(n2) or O(n log n).
# In the end, this algorithm will have the same order of magnitude as that
# of the checkoff process.




# ============================================================================ #
# Solution 3: Count and Compare
# ============================================================================ #

# Any two anagrams will have the same number of a’s, the same number of b’s,
# the same number of c’s, and so on.
# To decide whether two strings are anagrams, first count the number of times
# each character occurs.

def anagramSolution3(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagramSolution4('apple','pleap'))

# Again, the solution has a number of iterations.
# However, unlike the first solution, none of them are nested.

# The first two iterations used to count the characters are both based on n.
# The third iteration, comparing the two lists of counts, always takes 26 steps
# since there are 26 possible characters in the strings.
# Adding it all up gives us,
# T(n) = 2n + 26 steps.
# That is O(n).
# This is the linear order of magnitude algorithm for solving this problem.




# ============================================================================ #
# Ending Thoughts
# ============================================================================ #

# Although the last solution was able to run in linear time,
# it could only do so by using additional storage to keep the two lists of character counts.
# In other words, this algorithm sacrificed space in order to gain time.
