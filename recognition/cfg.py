#网络相关参数
height = 64
width = 128
label_len = 8
characters = '0123456789.-'+'|'  # recognition character 0 to 9, '|' for blank(ctc loss)
label_classes = len(characters)  # Number of categories requiring character recognition

ocr_dataset_path = r"Z:\Code\Python\datas\meter512\crnn_imgs"
train_txt_path = r"Z:\Code\Python\datas\meter512\crnn_train.txt"
val_txt_path = r"Z:\Code\Python\datas\meter512\crnn_val.txt"


#训练相关设置
checkpoint_path = "saved_model/weights_E{epoch:d}_L{loss:.5f}.h5"
saved_model_path = "saved_model/CRNN_model.h5"
saved_model_weights_path = "saved_model/CRNN_weights.h5"



