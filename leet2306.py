class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        res = 0
        dit = collections.defaultdict(set)
        for i in ideas:
            dit[i[0]].add(i[1:])
        temp = list(dit.keys())
        N = len(temp)
        for i in range(N):
            for j in range(i+1,N):
                common = len(dit[temp[i]] & dit[temp[j]])
                unique_one = len(dit[temp[i]]) - common
                unique_two = len(dit[temp[j]]) - common
                res += 2*unique_one*unique_two
        return res

        # res = 0
        # dit = collections.defaultdict(set)
        # for i in ideas:
        #     dit[i[0]].add(i[1:])
        # for i in dit.keys():
        #     for j in dit.keys():
        #         if i == j: continue
        #         common = len(dit[i] & dit[j])
        #         unique_one = len(dit[i]) - common
        #         unique_two = len(dit[j]) - common
        #         res += unique_one*unique_two
        # return res

        ## Suggested by Mr. Lokesh Chandak implemented by me
        # valid_names = set()
        # unique_initials = {i[0] for i in ideas}
        # unique_ends = {i[1:] for i in ideas}
        # unique_words = set()
        # ideas = set(ideas)
        # for i in unique_initials:
        #     for j in unique_ends:
        #         if i+j in ideas: continue
        #         unique_words.add(i+j)
        # for i in unique_words:
        #     for j in unique_words:
        #         if i == j: continue
        #         if i[0] + j[1:] in ideas and j[0] + i[1:] in ideas:
        #             valid_names.add(i+" "+j)
        # return len(valid_names)

        ##BRUTE FORCE
        # validName = set()
        # for i in ideas:
        #     for j in ideas:
        #         if i[0]+j[1:] in ideas or j[0]+i[1:] in ideas: continue
        #         validName.add(i[0]+j[1:]+" "+j[0]+i[1:])
        # return len(validName)
