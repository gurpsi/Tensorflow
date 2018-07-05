import tensorflow as tf

a = tf.constant(10)
b = tf.constant(20)

c = a*b

# If you want to see the Tensors:
print('Tensors: \n',a,b)

# If we want to run a computation graph:
ses = tf.Session()  # Creating a session object
print('\n On running the computational graph: \n',ses.run([c]))

# Visualising the graph:
File_Writer = tf.summary.FileWriter('C:\\Users\\gurpreet.ag.singh\\Desktop\\PyC\\Graph', ses.graph)

# to visualise open the terminal/Anaconda Prompt and navigate to the respective folder and run tensorboard --logdir = "PyC"

ses.close() # Freeing up the allocated resources by closing the object.

