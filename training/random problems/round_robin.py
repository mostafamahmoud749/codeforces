def round_robin(proces, arival_time, burst_time, time_quantum):
    n = len(proces)

    wait_time = 0
    turn_around_time = 0
    remaining_burst_time = burst_time[:]  
    start_time = [-1] * n  
    ready_queue = []  
    current_time = 0  
    completed = 0  
    
    for i in range(n):
        if arival_time[i] <= current_time:
            ready_queue.append(i)
    
    p = []

    while completed < n:
        if ready_queue:
            process = ready_queue.pop(0)  
            if start_time[process] == -1:
                start_time[process] = current_time
            
            time_to_run = min(time_quantum, remaining_burst_time[process])
            remaining_burst_time[process] -= time_to_run
            current_time += time_to_run 
            
            if remaining_burst_time[process] > 0:
                ready_queue.append(process)
            else:
                completed += 1
                wait_time += current_time - arival_time[process] - burst_time[process]
                turn_around_time += current_time - arival_time[process]
                p.append(proces[process]) 

        for i in range(n):
            if arival_time[i] <= current_time and i not in ready_queue and remaining_burst_time[i] > 0:
                ready_queue.append(i)

    avg_wait_time = wait_time / n
    avg_turnaround_time = turn_around_time / n
    
    print("Execution Order:", p)
    print("Average Waiting Time:", avg_wait_time)
    print("Average Turnaround Time:", avg_turnaround_time)

proces = ["p1", "p2", "p3", "p4"]
arival_time = [0, 1, 2, 3] 
burst_time = [6, 8, 7, 3]  
time_quantum = 4  

round_robin(proces, arival_time, burst_time, time_quantum)