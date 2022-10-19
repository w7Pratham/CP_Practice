class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dit = Counter(students)
        for ind, val in enumerate(sandwiches):
            if dit[val] == 0:
                return len(sandwiches)-ind
            dit[val] -= 1
        return 0
