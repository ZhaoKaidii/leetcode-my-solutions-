class Solution(object):
    def destCity(self, paths):
        dic={}
        for i in range(len(paths)):
            for j in range(0,2):
                if paths[i][j] not in dic:
                    dic[paths[i][j]]=(j+1)*0.1
                else:
                    dic[paths[i][j]]+=1
        for i in range(len(paths)):
            for  j in range(0,2):
                if dic[paths[i][j]]==0.2:
                    return paths[i][j]
