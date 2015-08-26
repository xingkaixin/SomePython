from task import add


taskid =  add.delay(4,14)
#taskid ='3e65d6b2-ddae-45ad-aaf4-8f1851171770'
print taskid
task = add.AsyncResult(taskid)
print task.state,task.get()
