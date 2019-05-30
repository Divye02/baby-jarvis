Taken from http://camdial.org/~mh521/dstc/

Things to Do:
- convert/verify that the ontology located in the scripts folder matches the ontologies of the woz file (they seem to be in a different format)
- create the WOZ equivalent of train, test, and dev data
- WOZ split = 600 train, 200 validation, 400 test

The converter script is located under the `scripts` folder

Notes:
- The `label.json` in the dstc2 data only contains the user utterances and the belief tracker state at each point of the user utterance
- There are a lot of turns where the user just says: "noise"
- The `log.json` has the actual info about what the system responds with