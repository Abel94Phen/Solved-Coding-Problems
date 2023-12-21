class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            image[row].reverse()
            for col in range(len(image)):
                image[row][col] = int(not image[row][col])
        return image
                