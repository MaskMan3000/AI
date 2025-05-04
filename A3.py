def prims_mst(n, cost, Nodes):
    visited = [False] * n
    min_cost = 0
   
    s = int(input(f"\nEnter Starting Vertex (1 to {n}): ")) - 1
    visited[s] = True
   
    print("\nSelected Edges in MST:")
   
    for _ in range(n - 1):
        min_edge = float('inf')
        row, col = -1, -1
       
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and cost[i][j] != -1 and cost[i][j] < min_edge:
                        min_edge = cost[i][j]
                        row, col = i, j
       
        if row != -1 and col != -1:
            print(f"Edge: {Nodes[row]} - {Nodes[col]}")
            min_cost += min_edge
            visited[col] = True
            cost[row][col] = -1
            cost[col][row] = -1
   
    print(f"\nTotal Min Cost: {min_cost}\n")



def main():
    n = int(input("\nEnter the number of Nodes: "))
    Nodes = []
   
    for i in range(n):
        city = input(f"Enter Node {i + 1}: ")
        Nodes.append(city)
   
    cost = [[0] * n for _ in range(n)]
   
    for i in range(n):
        for j in range(i + 1, n):
            op = input(f"\nIs there a connection between {Nodes[i]} and {Nodes[j]} (y/n)?: ").strip().lower()
            if op == 'y':
                cost[i][j] = cost[j][i] = int(input("Enter Cost: "))
            else:
                cost[i][j] = cost[j][i] = -1
   
    prims_mst(n, cost, Nodes)


if __name__ == "__main__":
    main()
