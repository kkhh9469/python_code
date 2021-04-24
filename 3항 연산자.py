# 3항 연산자
my_skill_tree = "".join([str1 for str1 in skill_tree if str1 in skill])
print(my_skill_tree)


# 위의 3항 현산자 풀이
for my_skill_tree in skill_trees:
        str2 = []
        
        for str1 in my_skill_tree:
            # print(str1)
            if str1 in skill:
                str2.append(str1)

	print(“”.join(str2))


# 결과
print(my_skill_tree) == print(“”.join(str2))