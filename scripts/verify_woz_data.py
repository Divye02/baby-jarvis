import codecs
import json
import pprint

data_path = "../data/woz/"

training_data = data_path + "woz_train_en.json"
validation_data = data_path + "woz_validate_en.json"
test_data = data_path + "woz_test_en.json"

# Given a dialogue json, returns a string combining all of the users cialogues
def get_user_dialogue(dialogue):
	user_dialogue = ""
	for turn in dialogue["dialogue"]:
		user_dialogue += " " + turn["transcript"]
	return user_dialogue

# Given a dialogue json, returns a list of the "inform" belief state at each
# turn of the dialogue
def get_belief_state(dialogue):
	belief_states = []

	for turn in dialogue["dialogue"]:
		belief_state = turn["belief_state"]

		turn_belief_state = []

		for belief in belief_state:
			# TODO: Consider "request" slots as well?
			if (belief['act'] == 'inform'):
				# Note: we can assume each belief has one slot
				slot = tuple(belief['slots'][0])
				turn_belief_state.append(slot)

		belief_states.append(turn_belief_state)

	return belief_states


def update_belief_slot_distribution(dialogue, storage):
	belief_state = get_belief_state(dialogue)
	belief_slots = []
	for turn in belief_state:
		turn_slots = []
		for belief in turn:
			turn_slots.append(belief[0])
		turn_slots.sort()
		turn_slots = tuple(turn_slots)
		if (turn_slots in storage):
			storage[turn_slots] += 1
		else:
			storage[turn_slots] = 1


training_json = json.load(codecs.open(training_data, "r", "utf-8"))
validation_json = json.load(codecs.open(validation_data, "r", "utf-8"))
test_json = json.load(codecs.open(test_data, "r", "utf-8"))

training_dialogues = set()

training_set_belief_distribution = {}
validation_set_belief_distribution = {}
test_set_belief_distribution = {}


for dialogue in training_json:
	training_dialogues.add(get_user_dialogue(dialogue))
	update_belief_slot_distribution(dialogue, training_set_belief_distribution)

train_validation_same = 0
for dialogue in validation_json:
	user_dialogue = get_user_dialogue(dialogue)
	if (user_dialogue in training_dialogues):
		train_validation_same += 1
	update_belief_slot_distribution(dialogue, validation_set_belief_distribution)

train_test_same = 0

for dialogue in test_json:
	user_dialogue = get_user_dialogue(dialogue)
	if (user_dialogue in training_dialogues):
		train_test_same += 1
	update_belief_slot_distribution(dialogue, test_set_belief_distribution)

# Stats on types of belief state slots (inform)
# Analysis on the max length

# How many dialogues are the same
print "Training Dialogues"
print len(training_json)

print "Validation Dialogues"
print len(validation_json)

print "Test Dialogues"
print len(test_json)

print "Same Dialogues Between Training and Validation"
print train_validation_same

print "Same Dialogues Between Training and Test"
print train_test_same

pp = pprint.PrettyPrinter(indent=4)
print "Training Data Slot Distribution"
pp.pprint(training_set_belief_distribution)

print "Validation Data Slot Distribution"
pp.pprint(validation_set_belief_distribution)

print "Test Data Slot Distribution"
pp.pprint(test_set_belief_distribution)
