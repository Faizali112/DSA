class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)== 2:
            return True
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        for i in range (2, len(coordinates)):
            new_x = coordinates[i][0]
            new_y = coordinates[i][1]
            if(y2-y1)*(new_x-x1) != (x2-x1)*(new_y-y1):
                return False
        return True

        