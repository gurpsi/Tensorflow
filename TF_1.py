import tensorflow as tf
sess = tf.Session()
a = tf.constant(50)
b = tf.constant(100)
print('Addition of 2 constant number:', sess.run(a+b))
print('Substraction of 2 constant numbers is:', sess.run(a-b))
print('Division of 2 constant numbers is:', sess.run(a/b))