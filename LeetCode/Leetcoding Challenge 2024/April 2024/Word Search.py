
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(i,j,word_idx):
            #we've reached the end of the word, meaning everything has matched until now
            if word_idx==len(word):
                return True
            
            #checking boundaries also checking if current idx matches the word_idx
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[word_idx]:
                return False
            current_word=board[i][j]
			
            #marking as visited
            board[i][j]='#'
			
			#traversing in all direction for the next word
            left=traverse(i,j-1,word_idx+1)
            right=traverse(i,j+1,word_idx+1)
            up=traverse(i-1,j,word_idx+1)
            down=traverse(i+1,j,word_idx+1)
            
            #removing the visited mark because it may be part of some other start
            board[i][j]=current_word
    
            return left or right or up or down
             
        
        for i in range(len(board)):
            for j in range(len(board[0])):
				#true only if the first word and other words are matching
                if board[i][j]==word[0] and traverse(i,j,0):
                    return True
					
		#the word was not matched
        return False
      
