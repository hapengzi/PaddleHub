#coding:utf-8
import paddle.fluid as fluid
import paddlehub as hub

# Load ERNIE pretrained model
module = hub.Module(name="ernie")
inputs, outputs, program = module.context(trainable=True, max_seq_len=128)

# Create ClassifyReader
reader = hub.reader.ClassifyReader(
    hub.dataset.ChnSentiCorp(), module.get_vocab_path(), max_seq_len=128)

# Create Text Classification Task
task = hub.create_text_cls_task(feature=outputs["pooled_output"], num_classes=2)

# Configure Fine-tune strategy
strategy = hub.AdamWeightDecayStrategy(learning_rate=5e-5)

# Setting runing config
config = hub.RunConfig(
    use_cuda=True, num_epoch=3, batch_size=32, strategy=strategy)
feed_list = [
    inputs["input_ids"].name, inputs["position_ids"].name,
    inputs["segment_ids"].name, inputs["input_mask"].name,
    task.variable("label").name
]

# Start fine-tuning
hub.finetune_and_eval(task, reader, feed_list, config)
