class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        loopCondition = False

        # Row Check
        for row in range(9):
            containsRowNumbers = set()
            for column in range(9):
                if ((board[row][column] not in containsRowNumbers)):
                    if (board[row][column] != "."):
                        containsRowNumbers.add(board[row][column])
                else:
                    return False

        # Column Check
        for column in range(9):
            containsColumnNumbers = set()
            for row in range(9):
                if ((board[row][column] not in containsColumnNumbers)):
                    if (board[row][column] != "."):
                        containsColumnNumbers.add(board[row][column])
                else:
                    return False

        # Square check (using integer division to determine boxes)
        """
        The Main Idea:
        ----------------------------
        1. Checking three boxes at a time (top three, then middle three, then bottom three) using sets
        2. For each column, we populate the respective set and check for duplicates
        3. For every three rows, reset the three sets and repeat the logic
        """
        setLeft = set()
        setMiddle = set()
        setRight = set()
        for row in range(9):
            if (row % 3 == 0):
                setLeft = set()
                setMiddle = set()
                setRight = set()
            for column in range(9):
                if (board[row][column] == "."):
                    continue
                if (column >= 0 and column <=2):
                    if (board[row][column] in setLeft):
                        return False
                    else:
                        setLeft.add(board[row][column])
                elif (column >= 3 and column <= 5):
                    if (board[row][column] in setMiddle):
                        return False
                    else:
                        setMiddle.add(board[row][column])
                else:
                    if (board[row][column] in setRight):
                        return False
                    else:
                        setRight.add(board[row][column])


        return True

            

            

            