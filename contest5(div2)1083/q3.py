t = int(input())
for _ in range(t):
    n = int(input())
    blogs = []
    for i in range(n):
        data = list(map(int, input().split()))
        li = data[0]
        blog = data[1:]
        blogs.append(blog)
    
    # Collect all users
    all_users = set()
    for blog in blogs:
        for user in blog:
            all_users.add(user)
    
    # Sort users for consistent mapping
    users_list = sorted(all_users)
    m = len(users_list)
    
    # Create mappings
    user_to_idx = {}
    for i in range(m):
        user_to_idx[users_list[i]] = i
    
    idx_to_user = {}
    for i in range(m):
        idx_to_user[i] = users_list[i]
    
    # Build graph
    adj = [[] for _ in range(m)]
    
    # Add edges: for each blog, first user must appear after others in final order
    for blog in blogs:
        first_idx = user_to_idx[blog[0]]
        for j in range(1, len(blog)):
            other_idx = user_to_idx[blog[j]]
            adj[other_idx].append(first_idx)
    
    # Remove duplicate edges
    for i in range(m):
        seen = set()
        unique = []
        for v in adj[i]:
            if v not in seen:
                seen.add(v)
                unique.append(v)
        adj[i] = unique
    
    # Calculate indegrees
    indeg = [0] * m
    for u in range(m):
        for v in adj[u]:
            indeg[v] += 1
    
    # Find nodes with indegree 0
    pq = []
    for u in range(m):
        if indeg[u] == 0:
            pq.append(u)
    
    # Topological sort with min-heap behavior
    result = []
    while pq:
        # Sort to get smallest first
        pq.sort()
        u = pq.pop(0)
        result.append(u)
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                pq.append(v)
    
    # Convert back to original user IDs
    output = [idx_to_user[x] for x in result]
    print(' '.join(map(str, output)))