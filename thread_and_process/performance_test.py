import multiprocessing
import threading
import time

g_queue = multiprocessing.Queue()


def init_queue():
    print("init g_queue start")
    while not g_queue.empty():
        g_queue.get()
    for index in range(10):
        g_queue.put(index)
    print("init g_queue end")
    return


# 定义一个IO密集型任务：利用time.sleep()
def task_io(task_id):
    print("IOTask[%s] start" % task_id)
    while not g_queue.empty():
        time.sleep(1)
        try:
            data = g_queue.get(block=True, timeout=1)
            print("IOTask[%s] get data: %s" % (task_id, data))
        except Exception as e:
            print("IOTask[%s] error: %s" % (task_id, str(e)))
    print("IOTask[%s] end" % task_id)
    return


g_search_list = list(range(10000))


# 定义一个计算密集型任务：利用一些复杂加减乘除、列表查找等
def task_cpu(task_id):
    print("CPUTask[%s] start" % task_id)
    while not g_queue.empty():
        count = 0
        for i in range(10000):
            count += pow(3 * 2, 3 * 2) if i in g_search_list else 0
            # print(count)
        try:
            data = g_queue.get(block=True, timeout=1)
            print("CPUTask[%s] get data: %s" % (task_id, data))
        except Exception as e:
            print("CPUTask[%s] error: %s" % (task_id, str(e)))
    print("CPUTask[%s] end" % task_id)
    return task_id


if __name__ == "__main__":
    print("cpu count:", multiprocessing.cpu_count(), "\n")

    print("===== run io task directly =====")
    init_queue()
    time_0 = time.time()
    task_io(0)
    print("end: ", time.time() - time_0, "\n")

    print("===== run io task by multi thread =====")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=task_io, args=(i,)) for i in range(5)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    print("end: ", time.time() - time_0, "\n")

    print("===== run io task by multiprocess =====")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=task_io, args=(i,)) for i in range(multiprocessing.cpu_count())]
    for p in process_list:
        p.start()
    for p in process_list:
        if p.is_alive():
            p.join()
    print("结束: ", time.time() - time_0, "\n")

    print("===== run cpu task directly =====")
    init_queue()
    time_0 = time.time()
    task_cpu(0)
    print("end: ", time.time() - time_0, "\n")

    print("===== run cpu task by multi thread =====")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=task_cpu, args=(i,)) for i in range(5)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    print("end: ", time.time() - time_0, "\n")

    print("===== run cpu task by multiprocess =====")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=task_cpu, args=(i,)) for i in range(multiprocessing.cpu_count())]
    for p in process_list:
        p.start()
    for p in process_list:
        if p.is_alive():
            p.join()
    print("end: ", time.time() - time_0, "\n")
