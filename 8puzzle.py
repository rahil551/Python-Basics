class solution:
     def solve(self,board):
         dict = {}
         flatten = []
         for i in range(len(board)):
             flatten += board[i]
         flatten = tuple(flatten)
         dict[flatten] = 0
         if flatten == (0,1,2,3,4,5,6,7,8):
             return 0
         return self.get_paths(dict)
     def get_paths(self,dict):
         cnt = 0
         while True:
             current_nodes = [x for x in dict if dict[x]== cnt]
             if(len(current_nodes))==0:
                 return -1
             for node in current_nodes:
                 next_moves = self.find_next(node)
                 for move in next_moves:
                     if move not in dict:
                         dict[move] = cnt +1
             cnt+=1            