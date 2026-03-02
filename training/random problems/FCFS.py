def FCFS(proces, arival_time, burst_time):
    n = len(proces)
    wait_time = 0
    turn_around_time = 0
    start_time = [0] * n

    p = []

    for i in range(n):
        if i == 0:
            start_time[i] = arival_time[i]  
        else:
            start_time[i] = max(arival_time[i], start_time[i-1] + burst_time[i-1])  
        

        wait_time += start_time[i] - arival_time[i]
        turn_around_time += start_time[i] + burst_time[i] - arival_time[i]

        p.append(proces[i])
    
    avg_wait_time = wait_time / n
    avg_turnaround_time = turn_around_time / n
    
    print("Execution Order:", p)
    print("Average Waiting Time:", avg_wait_time)
    print("Average Turnaround Time:", avg_turnaround_time)

proces = ["p1", "p2", "p3", "p4"]
arival_time = [0, 1, 2, 3]
burst_time = [6, 8, 7, 3]

FCFS(proces, arival_time, burst_time)