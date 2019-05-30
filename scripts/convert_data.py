# Script to convert dstc2 data to woz data
# So we can train it
import codecs
import json
import os
import pprint

data_path = "../data/dstc2/"
# Change for training vs. test data
data_type = "dstc2_test"


"""
SAMPLE WOZ DIALOGUE:
 dialogue_idx = generate by our self
 dialogue
 	- turn_label = goal-labels
 	- asr = transcription 
 	- system_transcript = 
 	- turn_idx
 	- belief_state
 	- transcript
 	- system_acts
{
        "dialogue_idx": 800, 
        "dialogue": [
            {
                "turn_label": [
                    [
                        "area", 
                        "east"
                    ], 
                    [
                        "price range", 
                        "cheap"
                    ], 
                    [
                        "request", 
                        "phone"
                    ], 
                    [
                        "request", 
                        "postcode"
                    ]
                ], 
                "asr": [
                    [
                        "What is the phone number and postcode of a cheap restaurant in the east part of town?", 
                        1.0
                    ]
                ], 
                "system_transcript": "", 
                "turn_idx": 0, 
                "belief_state": [
                    {
                        "slots": [
                            [
                                "slot", 
                                "phone"
                            ]
                        ], 
                        "act": "request"
                    }, 
                    {
                        "slots": [
                            [
                                "slot", 
                                "postcode"
                            ]
                        ], 
                        "act": "request"
                    }, 
                    {
                        "slots": [
                            [
                                "price range", 
                                "cheap"
                            ]
                        ], 
                        "act": "inform"
                    }, 
                    {
                        "slots": [
                            [
                                "area", 
                                "east"
                            ]
                        ], 
                        "act": "inform"
                    }
                ], 
                "transcript": "What is the phone number and postcode of a cheap restaurant in the east part of town?", 
                "system_acts": []
            }...
    }
"""

path = data_path + data_type + "/data"
dialogues = [x[0] for x in os.walk(path)]

for d in dialogues:
	labeled_data = d + "/label.json"
	print(d)
	try:
		j = json.load(codecs.open(labeled_data, "r", "utf-8"))
		print(j['turns'][1])
	except:
		# This folder did not have a label.json file, ignore and continue
		continue

