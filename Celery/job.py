from task import add,minus


taskid =  add.delay(4,14)
# taskid ='3e65d6b2-ddae-45ad-aaf4-8f1851171770'
print taskid
# task = add.AsyncResult(taskid)
# print task.state,task.get()
taskid2 = minus.delay(10,5)
print taskid2

# taskid ='99b0d2c5-7dae-4cf3-90ec-962b4db7c323'
# task = add.AsyncResult(taskid)
# print task.state


for i in range(1,100):
    taskid =  add.delay(4,14)
    # taskid ='3e65d6b2-ddae-45ad-aaf4-8f1851171770'
    print taskid
    # task = add.AsyncResult(taskid)
    # print task.state,task.get()
    taskid2 = minus.delay(10,5)
    print taskid2
