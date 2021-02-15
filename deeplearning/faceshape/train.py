import os

import matplotlib
import matplotlib.pylab as plt

from deeplearning.faceshape.utils import getTimeFolderName

matplotlib.use('TkAgg')
import numpy as np

import tensorflow as tf
import tensorflow_hub as hub

print("TF version:", tf.__version__)
print("Hub version:", hub.__version__)
print("GPU is", "available" if tf.test.is_gpu_available() else "NOT AVAILABLE")

# set environment variables TFHUB_CACHE_DIR
# module_selection = ("mobilenet_v2_100_224", 224)
module_selection = ("inception_v3", 299)

handle_base, pixels = module_selection
MODULE_HANDLE = "https://tfhub.dev/google/imagenet/{}/feature_vector/4".format(handle_base)

IMAGE_SIZE = (pixels, pixels)
print("Using {} with input size {}".format(MODULE_HANDLE, IMAGE_SIZE))

foldername = getTimeFolderName()
saved_model_path = os.getcwd() + "/saved_models/" + foldername
fine_tune_model_path = os.getcwd() + "/fine_tune_models/" + foldername
do_fine_training_on_this_model=os.getcwd() + "/saved_models/" + "2021-02-10_16-50-20/"

is_fine_tune_enabled = False
BATCH_SIZE = 32
initial_epochs = 3
fine_tune_epochs = 2
base_learning_rate = 0.005
do_data_augmentation = False

data_dir = "/home/ashish/Downloads/FaceShape Dataset/testing_set"
datagen_kwargs = dict(rescale=1. / 255, validation_split=.20)
dataflow_kwargs = dict(target_size=IMAGE_SIZE, batch_size=BATCH_SIZE,
                       interpolation="bilinear")

valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    **datagen_kwargs)
valid_generator = valid_datagen.flow_from_directory(
    data_dir, subset="validation", shuffle=True, **dataflow_kwargs)

if do_data_augmentation:
    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=40,
        horizontal_flip=True,
        width_shift_range=0.2, height_shift_range=0.2,
        shear_range=0.2, zoom_range=0.2,
        **datagen_kwargs)
else:
    train_datagen = valid_datagen
train_generator = train_datagen.flow_from_directory(
    data_dir, subset="training", shuffle=True, **dataflow_kwargs)

steps_per_epoch = train_generator.samples // train_generator.batch_size
validation_steps = valid_generator.samples // valid_generator.batch_size


def train():
    pretrained_thub_layers = hub.KerasLayer(MODULE_HANDLE, trainable=False)

    print("Building model with", MODULE_HANDLE)
    model = tf.keras.Sequential([
        # Explicitly define the input shape so the model can be properly
        # loaded by the TFLiteConverter
        tf.keras.layers.InputLayer(input_shape=IMAGE_SIZE + (3,)),
        pretrained_thub_layers,
        tf.keras.layers.Dropout(rate=0.2),  ##prevent overfitting
        tf.keras.layers.Dense(train_generator.num_classes,
                              kernel_regularizer=tf.keras.regularizers.l2(0.0001), activation='softmax')
        ##softmax increase probility on one by decresing others low probabilty
    ])

    model.build((None,) + IMAGE_SIZE + (3,))
    print("####### printing first time model summary###############")

    model.summary()

    model.compile(
        optimizer=tf.keras.optimizers.SGD(lr=base_learning_rate, momentum=0.9),
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True, label_smoothing=0.1),
        metrics=['accuracy'])

    print("steps_per_epoch", steps_per_epoch, "validation_steps", validation_steps)
    history = model.fit(
        train_generator,
        epochs=initial_epochs, steps_per_epoch=steps_per_epoch,
        validation_data=valid_generator,
        validation_steps=validation_steps)

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']
    plotHistogram(acc, val_acc, loss, val_loss)

    os.makedirs(saved_model_path)

    tf.saved_model.save(model, saved_model_path)

    if not is_fine_tune_enabled:
        return
    # finetuning #############
    pretrained_thub_layers.trainable = True

    model.compile(
        optimizer=tf.keras.optimizers.SGD(lr=base_learning_rate / 10, momentum=0.9),
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True, label_smoothing=0.1),
        metrics=['accuracy'])

    # printing fine tuning model summary
    print("####### printing fine tuning model summary###############")
    model.summary()

    total_epochs = initial_epochs + fine_tune_epochs

    history_fine = model.fit(
        train_generator,
        epochs=total_epochs, steps_per_epoch=steps_per_epoch,
        initial_epoch=history.epoch[-1],
        validation_data=valid_generator,
        validation_steps=validation_steps)

    acc += history_fine.history['accuracy']
    val_acc += history_fine.history['val_accuracy']

    loss += history_fine.history['loss']
    val_loss += history_fine.history['val_loss']

    plotHistogramFineTuning(acc, val_acc, loss, val_loss)
    os.makedirs(fine_tune_model_path)

    tf.saved_model.save(model, fine_tune_model_path)


def plotHistogram(acc, val_acc, loss, val_loss):
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.ylabel('Accuracy')
    plt.ylim([min(plt.ylim()), 1])
    plt.title('Training and Validation Accuracy')

    plt.subplot(2, 1, 2)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.ylabel('Cross Entropy')
    plt.ylim([0, 1.0])
    plt.title('Training and Validation Loss')
    plt.xlabel('epoch')
    plt.show()


def plotHistogramFineTuning(acc, val_acc, loss, val_loss):
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.ylim([0.8, 1])
    plt.plot([initial_epochs - 1, initial_epochs - 1],
             plt.ylim(), label='Start Fine Tuning')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(2, 1, 2)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.ylim([0, 1.0])
    plt.plot([initial_epochs - 1, initial_epochs - 1],
             plt.ylim(), label='Start Fine Tuning')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.xlabel('epoch')
    plt.show()


def get_class_string_from_index(index):
    for class_string, class_index in valid_generator.class_indices.items():
        if class_index == index:
            return class_string


def inference():
    x, y = next(valid_generator)
    print(y)
    image = x[21, :, :, :]
    # true_index = np.argmax(y[0])
    # plt.imshow(image)
    # plt.axis('off')
    # plt.show()
    i = 0
    image = x[i, :, :, :]
    true_index = np.argmax(y[i])
    # Expand the validation image to (1, 224, 224, 3) before predicting the label
    model = tf.keras.models.load_model(saved_model_path)
    prediction_scores = model.predict(np.expand_dims(image, axis=0))
    predicted_index = np.argmax(prediction_scores)
    print("True label: " + get_class_string_from_index(true_index))
    print("Predicted label: " + get_class_string_from_index(predicted_index))


def inferenceOnBatch():
    x, y = next(valid_generator)
    # Expand the validation image to (1, 224, 224, 3) before predicting the label
    model = tf.keras.models.load_model(saved_model_path)
    for i, xx in enumerate(x):
        x[i] = np.expand_dims(xx, axis=0)

    prediction_scores = model.predict_on_batch(x)
    for i, ps in enumerate(prediction_scores):
        true_index = np.argmax(y[i])
        predicted_index = np.argmax(ps)
        print("True label: " + get_class_string_from_index(true_index))
        print("Predicted label: " + get_class_string_from_index(predicted_index))
        print()


def fine_tune_model(model_path):
    model = tf.keras.models.load_model(model_path)
    model.training = True
    model.compile(
        optimizer=tf.keras.optimizers.SGD(lr=base_learning_rate / 10, momentum=0.9),
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True, label_smoothing=0.1),
        metrics=['accuracy'])
    model.summary()
    history = model.fit(
        train_generator,
        epochs=fine_tune_epochs, steps_per_epoch=steps_per_epoch,
        validation_data=valid_generator,
        validation_steps=validation_steps)

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']
    plotHistogram(acc, val_acc, loss, val_loss)

    os.makedirs(fine_tune_model_path)
    tf.saved_model.save(model, fine_tune_model_path)


# train()
fine_tune_model(do_fine_training_on_this_model)
# inferenceOnBatch()
# inference()
