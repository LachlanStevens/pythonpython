import json
import random
def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))
    i = [0,3,4,5,32,3,4,5]
    print("THIS IS MY DEBUGINGGINGINGINGIN")
    print("made it to this line!!! thanks stackery")
    
    return {
        "testing": random.choice(i)
    }
