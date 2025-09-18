
# deep learning  = duplication of human brain

# analyze small details
# combine into parts
# understand the whole

# deep deep deep layers
# simple features
# complex shapes
# full recognition

# a computer learning step by step with many layeres just like human brain



import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import models, layers

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

X_train=X_train.reshape(-1,28,28,1)
X_test=X_test.reshape(-1,28,28,1) 

model=models.Sequential([
    layers.Conv2D(32,(3,3), activation='relu',input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64,activation='relu'),
    layers.Dense(10,activation='softmax')
])
model.compile(optimizer='adam',
           loss="sparse_categorical_crossentropy",
           metrics=['accuracy']   )

history=model.fit(
X_train,y_train,
epochs=5,
batch_size=64,
validation_data=(X_test,y_test),
verbose=1
)

test_loss,test_acc=model.evaluate(X_test,y_test,verbose=0)
print("Test Accuracy:", round(test_acc * 100,2),"%")

prediction=model.predict(X_test[:1])
predicted_label=prediction.argmax()

plt.imshow(X_test[0].reshape(28,28),cmap="grey")
plt.title("prediction:"+str(predicted_label))
plt.axis("off")
plt.show()