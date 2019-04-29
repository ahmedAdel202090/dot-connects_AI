from dotconnect import play
from searchoptimize import search
#level 1 solved
if __name__ == '__main__':
    rows=int(input("enter board rows :"))
    cols=int(input("enter board cols :"))
    num_obstacles=int(input("enter a number of obstacles:"))
    obstacles=[]
    for i in range(num_obstacles):
        print("enter obstacle at ",i)
        obs0=int(input())
        obs1=int(input())
        obstacles.append([obs0,obs1])
    search_res=search(rows,cols,obstacles)
    play(search_res[0],rows,cols,search_res[1])
