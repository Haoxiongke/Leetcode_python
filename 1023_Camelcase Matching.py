'''
Question:
A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.

Example 1:
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
'''


def camelMatch(queries, pattern):
    '''
    驼峰式匹配
    :param queries:
    :param pattern:
    :return:
    '''
    res,length = list(),len(pattern)
    for query in queries:
        isValid, current_index = True, 0
        for ch in query:
            if current_index < length and ch == pattern[current_index]:
                current_index += 1
            elif ch.isupper():
                isValid = False
                break
        res.append(True if isValid and length == current_index  else False)
    return res

if __name__ == "__main__":
    print(camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))
