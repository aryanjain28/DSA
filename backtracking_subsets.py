dfs(index = 0, path = [], res = [])
|
|__ dfs(index = 1 , path = [1], res = [[]])
|    |__ dfs(index = 2 , path = [1,2], res = [[],[1]])
|    |    |__ dfs(index = 3, path = [1,2,3], res = [[],[1],[1,2]])
|    |         # next: res = [[],[1],[1,2],[1,2,3]]
|    |         # for loop will not be executed
|    |
|    |__ dfs(index = 3 , path = [1,3], res = [[],[1],[1,2],[1,2,3]])
|    	  	   # next: res = [[],[1],[1,2],[1,2,3],[1,3]]
|    	  	   # for loop will not be executed
|
|__ dfs(index = 2, path = [2], res = [[],[1],[1,2],[1,2,3],[1,3]])
|    |__ dfs(index = 3 , path = [2,3], res = [[],[1],[1,2],[1,2,3],[1,3],[2]])
|    	  	   # next iteration: res =  [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3]]
|    	  	   # for loop will not be executed
|
|__ dfs(index = 3, path = [3], res =  [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3]])
     	  	   # next iteration: res =  [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
     	  	   # for loop will not be executed