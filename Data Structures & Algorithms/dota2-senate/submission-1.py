class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q, d_q = deque(), deque()

        for i in range(len(senate)):
            m = senate[i]
            if m =="R":
                r_q.append(i)
            else:
                d_q.append(i)

        while True:
            if len(r_q)==0:
                return "Dire"
            if len(d_q)==0:
                return "Radiant"
            
            r, d = r_q.popleft(), d_q.popleft()

            print(r, d)
            if r<d:
                print("D at index",d, "is out")
                r_q.append(len(senate)+r)
            else:
                print("R at index",r, "is out")
                d_q.append(len(senate)+d)


        