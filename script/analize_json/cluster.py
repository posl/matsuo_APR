import csv

class Cluster:
    def __init__(self):
        #キーワードリストを生成
        self.lect_dic = {}
        with open("keyword.csv","r",encoding='utf-8') as f:
            infile = csv.reader(f)
            for line in infile:
                self.lect_dic[line[0]]=line[1:]
            print(self.lect_dic)

    def cluster(self,code):
        Max_id = 'other'
        Max_w = 0
        Max_p = 0
        for key in self.lect_dic:
            weight = int(self.lect_dic[key][0])
            p = count_point(code,self.lect_dic[key][1:])
            if p==0:
                continue
            else:
                if Max_w < weight:
                    Max_id = key
                    Max_p = p
                    Max_w = weight
                elif Max_w==weight:
                    if p>Max_p:
                        Max_id = key
                        Max_p = p
                        Max_w = weight
        return Max_id
                    
def count_point(code,lis):
    p = 0
    for l in lis:
        if l in code:
            p+=1
    return p

