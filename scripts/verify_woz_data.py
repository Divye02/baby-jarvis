import json
import codecs

data_path = "../data/woz/"

training_data = data_path + "woz_train_en.json"
validation_data = data_path + "woz_validate_en.json"
test_data = data_path + "woz_test_en.json"

training_json = json.load(codecs.open(training_data, "r", "utf-8"))
training_dialogues = set()
for dialogue in training_json:
	training_dialogues.add(dialogue["dialogue"][0]["asr"][0][0])

validation_json = json.load(codecs.open(validation_data, "r", "utf-8"))

same_count = 0
validation_count = 0

for dialogue in validation_json:
	first_dialogue = dialogue["dialogue"][0]["asr"][0][0]
	validation_count += 1
	if (first_dialogue in training_dialogues):
		print first_dialogue
		same_count += 1

# Stats on types of belief state slots (inform)
# Analysis on the max length

# Train and Validation
print "Training Dialogues"
print len(training_dialogues)

print "Validation Dialogues"
print validation_count

print "Same First Dialogues Between Training and Validation"
print same_count
