#!/usr/bin/env python

import sys

def build_matrix(n,m):

    '''Build a nxm matrix with first row = [0,1,2..m-1] and first col = [0,1,2..n-1]'''

    matrix = [[i for i in range(m)]]
    row = [0 for i in range(m)]
    for i in range(1,n):
        matrix.append(row[:])
        matrix[i][0] = i

    return matrix

def print_matrix(mat):
    '''Print matrix in formatted rows'''
    for col in mat:
        print col

def distance(src,dest):
    '''Calculate Levenshtein distance'''
    n = len(src)
    m = len(dest)

    matrix = build_matrix(n+1,m+1)
    for i in range(1,n+1):
        for j in range(1,m+1):
            cost = int( (ord(src[i-1]) - ord(dest[j-1]))!= 0)
            v1 = matrix[i-1][j] + 1 
            v2 = matrix[i][j-1] + 1
            v3 = matrix[i-1][j-1] + cost

            matrix[i][j] = min(v1,v2,v3)
    return matrix[n][m]



def dictparse(filename):
    '''Parse words from dictionary and build a hash for reduce word comparisons'''
    f = open(filename)
    wordsmap = {}
    
    for word in f:
        
        word = word.strip('\r\n')
        length = len(word)
        if not wordsmap.has_key(length):
            wordsmap[length] = []
    
        wordsmap[length].append(word)

    return wordsmap


def spellcheck(word,wordsmap):
    '''Perform spellcheck and provide word suggestions'''
    minword = ''
    errors = []
    length = len(word)
    if length == 1:
        return None
    selected_set = wordsmap[length] + wordsmap[length+1]
    dist = 1000
    if word in wordsmap[length]:
        return None

    for w in selected_set:
        calcdist = distance(word,w)

        if calcdist < 2:
            errors.append(w)

    return errors




wordsmap = dictparse('Dictionary.txt')
line = raw_input("Input Line: ") 

        
for w in line.split(' '):
    result = spellcheck(w,wordsmap)

    if result != None:
           print w,"(",",".join(result),")",
    else:
           print w

        
