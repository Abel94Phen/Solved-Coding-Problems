class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ave_skill = 2 * sum(skill) / len(skill)
        chemistry = 0
        for i in range(len(skill)//2):
            if skill[i] + skill[len(skill) - i - 1] != ave_skill:
                return -1
            chemistry += skill[i] * skill[len(skill) - i - 1]
        return chemistry