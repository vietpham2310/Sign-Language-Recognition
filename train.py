import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format

# step 2 =======================


WORKSPACE_PATH = 'G:/ForPushGit/Sign-Language-Recognition/Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
APIMODEL_PATH = 'Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
#CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/ssd_mobnet_ckp_alphabet/'

# step 2 =======================
CUSTOM_MODEL_NAME = 'ssd_mobnet_ckp_alphabet'
CONFIG_PATH = MODEL_PATH+'/'+CUSTOM_MODEL_NAME+'/pipeline.config'
config = config_util.get_configs_from_pipeline_file(CONFIG_PATH)



pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
with tf.io.gfile.GFile(CONFIG_PATH, "r") as f:
    proto_str = f.read()
    text_format.Merge(proto_str, pipeline_config)
#
#
pipeline_config.model.ssd.num_classes = 25
pipeline_config.train_config.batch_size = 4
pipeline_config.train_config.fine_tune_checkpoint = PRETRAINED_MODEL_PATH+'/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/checkpoint/ckpt-0'
pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
pipeline_config.train_input_reader.label_map_path= ANNOTATION_PATH + '/label_map2.pbtxt'
pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [ANNOTATION_PATH + '/train_alpha.record']
pipeline_config.eval_input_reader[0].label_map_path = ANNOTATION_PATH + '/label_map2.pbtxt'
pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [ANNOTATION_PATH + '/test_alpha.record']

config_text = text_format.MessageToString(pipeline_config)
with tf.io.gfile.GFile(CONFIG_PATH, "wb") as f:
    f.write(config_text)

# step 2 =======================
# ===== step 1 =====
# labels = [{'name':'where', 'id':1},
#           {'name':'work', 'id':2},
#           {'name':'your', 'id':3},
#           {'name':'you', 'id':4},
#           {'name':'yes', 'id':5},]

# labels = [{'name':'b', 'id':1},
#           {'name':'c', 'id':2},]

# labels = [{'name':'??? ????u', 'id':1},
#           {'name':'l??m', 'id':2},
#           {'name':'c???a b???n', 'id':3},
#           {'name':'b???n', 'id':4},
#           {'name':'c??', 'id':5},]

# labels = [{'name':'nh?? v??? sinh', 'id':1},
#           {'name':'?????n t???', 'id':2},
#           {'name':'t???m bi???t', 'id':3},
#           {'name':'xin ch??o', 'id':4},
#           {'name':'l??m th??? n??o', 'id':5},
#           {'name':'b???n d???o n??y th??? n??o', 'id':6},
#           {'name':'t??i', 'id':7},
#           {'name':'anh y??u em', 'id':8},
#           {'name':'t??i ???n', 'id':9},
#           {'name':'??ang h???c', 'id':10},
#           {'name':'ngh??a l?? g??', 'id':11},
#           {'name':'g???p b???n', 'id':12},
#           {'name':'c???a t??i', 'id':13},
#           {'name':'t??n', 'id':14},
#           {'name':'r???t vui ???????c', 'id':15},
#           {'name':'kh??ng', 'id':16},
#           {'name':'k?? hi???u', 'id':17},
#           {'name':'????nh v???n', 'id':18},
#           {'name':'c???m ??n', 'id':19},
#           {'name':'gi??? l?? m???y gi??? th???', 'id':20},
#           {'name':'l?? g??', 'id':21},
#           {'name':'????u', 'id':22},
#           {'name':'c??', 'id':23},
#           {'name':'b???n', 'id':24},
#           {'name':'c???a b???n', 'id':25},]

# labels = [{'name':'a', 'id':1},
#           {'name':'b', 'id':2},
#           {'name':'c', 'id':3},
#           {'name':'d', 'id':4},
#           {'name':'??', 'id':5},
#           {'name':'dm', 'id':6},
#           {'name':'dr', 'id':7},
#           {'name':'e', 'id':8},
#           {'name':'g', 'id':9},
#           {'name':'h', 'id':10},
#           {'name':'i', 'id':11},
#           {'name':'k', 'id':12},
#           {'name':'l', 'id':13},
#           {'name':'m', 'id':14},
#           {'name':'n', 'id':15},
#           {'name':'o', 'id':16},
#           {'name':'p', 'id':17},
#           {'name':'q', 'id':18},
#           {'name':'r', 'id':19},
#           {'name':'s', 'id':20},
#           {'name':'t', 'id':21},
#           {'name':'u', 'id':22},
#           {'name':'v', 'id':23},
#           {'name':'x', 'id':24},
#           {'name':'y', 'id':25},]

# labels = [{'name':'nh?? v??? sinh', 'id':1},
#           {'name':'xin l???i ???? l??m phi???n', 'id':2},
#           {'name':'s??? th??ch', 'id':3},
#           {'name':'t??? ????u', 'id':4},
#           {'name':'t???m bi???t', 'id':5},
#           {'name':'xin ch??o', 'id':6},
#           {'name':'n??y b???n ??i', 'id':7},
#           {'name':'l??m th??? n??o', 'id':8},
#           {'name':'b???n d???o n??y th??? n??o', 'id':9},
#           {'name':'t??i', 'id':10},
#           {'name':'anh y??u em', 'id':11},
#           {'name':'t??i ???n', 'id':12},
#           {'name':'l???i sau', 'id':13},
#           {'name':'??ang h???c', 'id':14},
#           {'name':'c???a b???n', 'id':15},
#           {'name':'b???n', 'id':16},
#           {'name':'c??', 'id':17},
#           {'name':'??? ????u', 'id':18},
#           {'name':'l??m c??i g??', 'id':19},
#           {'name':'c??i g??', 'id':20},
#           {'name':'m???y gi???', 'id':21},
#           {'name':'c???m ??n', 'id':22},
#           {'name':'gi??? s???c kh???e', 'id':23},
#           {'name':'????nh v???n', 'id':24},
#           {'name':'k?? hi???u', 'id':25},
#           {'name':'h???n g???p', 'id':26},
#           {'name':'l??m ??n', 'id':27},
#           {'name':'kh??ng', 'id':28},
#           {'name':'r???t vui', 'id':29},
#           {'name':'t??n', 'id':30},
#           {'name':'c???a t??i', 'id':31},
#           {'name':'g???p b???n', 'id':32},
#           {'name':'?? ngh??a', 'id':33},
#           {'name':'th??ch', 'id':34},
#           {'name':'l??m', 'id':35},]
#           {'name':'a', 'id':36},
#           {'name':'b', 'id':37},
#           {'name':'c', 'id':38},
#           {'name':'d', 'id':39},
#           {'name':'e', 'id':40},
#           {'name':'g', 'id':41},
#           {'name':'h', 'id':42},
#           {'name':'i', 'id':43},
#           {'name':'k', 'id':44},
#           {'name':'l', 'id':45},
#           {'name':'m', 'id':46},
#           {'name':'n', 'id':47},
#           {'name':'o', 'id':48},
#           {'name':'p', 'id':49},
#           {'name':'q', 'id':50},
#           {'name':'r', 'id':51},
#           {'name':'s', 'id':52},
#           {'name':'t', 'id':53},
#           {'name':'u', 'id':54},
#           {'name':'v', 'id':55},
#           {'name':'x', 'id':56},
#           {'name':'y', 'id':57},
#           {'name':'??', 'id':58},]
# #
# with open(ANNOTATION_PATH + '\label_map2.pbtxt', 'w', encoding='utf-8') as f:
#     for label in labels:
#         f.write('item { \n')
#         f.write('\tname:\'{}\'\n'.format(label['name']))
#         f.write('\tid:{}\n'.format(label['id']))
#         f.write('}\n')

# ===== step 1 =====
print("smt")

# !python {SCRIPTS_PATH + '/generate_tfrecord.py'} -x {IMAGE_PATH + '/train'} -l {ANNOTATION_PATH + '/label_map.pbtxt'} -o {ANNOTATION_PATH + '/train.record'}
# !python {SCRIPTS_PATH + '/generate_tfrecord.py'} -x{IMAGE_PATH + '/test'} -l {ANNOTATION_PATH + '/label_map.pbtxt'} -o {ANNOTATION_PATH + '/test.record'}